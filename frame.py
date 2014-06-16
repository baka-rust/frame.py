import re, os
from wsgiref.simple_server import make_server

class Frame:
	
	def __init__(self, urlPatterns=[], staticDir = "static/"):
		self.urlPatterns = urlPatterns
		self.staticDir = staticDir
		if staticDir:
			self.urlPatterns.insert(0, ("^/static/(.*)$", self.staticUrl))
	
	def route(self, pattern):
		def decorator(method):
			self.urlPatterns.append((pattern, method))
			return method
		return decorator
	
	def handleUrl(self, environmentVariables):
		url = environmentVariables["PATH_INFO"]
		if len(url) > 1 and url[-1] == '/':
			url = url[:-1]
		for rule in self.urlPatterns:
			result = re.search(rule[0], url)
			if result:
				if len(result.groups()) > 0:
					return rule[1](Request(environmentVariables, result)) #accomidate multiple captures
				else:
					return rule[1](Request(environmentVariables, None))
		raise Http404
		
	def staticUrl(self, request):
		path = request.capturedData.group(1)
		try:
			f = open(self.staticDir+path, 'rb')
			return Response(f.read(), "static")
		except:
			raise Http404
		
	def application(self, environmentVariables, startResponse):
		status = '200 OK'
		responseHeaders = [('Content-Type', 'text/html')]
		try:
			response = self.handleUrl(environmentVariables)
			responseBody = response.body
			if response.type == "static":
				responseHeaders = [('Content-Type', '')]
		except Http404:
			status = '404 Not Found'
			responseBody = 'Not found: ' + environmentVariables['PATH_INFO'] # custom 404 page?
		except Redirect, e:
			status = '301 Moved Permanently'
			responseHeaders.append(('Location', e.location))
			responseBody = ''
		responseHeaders.append(('Content-Length', str(len(responseBody))))

		startResponse(status, responseHeaders)
		return [responseBody]
	
	def testServer(self, port):
		httpd = make_server('localhost', port, self.application)
		print "frame.py development server started on " + str(port)
		print "use CTRL-BREAK to end server"
		while True:
			httpd.handle_request()

class Request:
	def __init__(self, environmentVariables, capturedData):
		self.type = environmentVariables["REQUEST_METHOD"]
		self.environmentVariables = environmentVariables
		self.capturedData = capturedData

class Response:
	def __init__(self, body, type="dynamic", status="200 OK"):
		self.body = body
		self.type = type
		self.status = status
				
class Http404(Exception):
	pass
	
class Redirect(Exception):
	def __init__(self, location):
		self.location = location