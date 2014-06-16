from frame import Frame, Response, Http404, Redirect

# views
def index(request):
	return Response("hello world.") # call frame.render on template here
	
def count(request):
	if request.type == "GET":
		return Response("you entered " + str(request.capturedData.group(1)))
	else:
		raise Http404
	
# urls
urlPatterns = [
	("^/$", index),
	("^/count/([1-9]*)$", count),
]

# app running
app = Frame(urlPatterns)
#app.testServer(80)