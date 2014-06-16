import frame

# views
def index(request):
	return "hello world." # call frame.render on template here
	
def count(request):
	if request.type == "GET":
		return "you entered " + str(request.capturedData)
	else:
		raise frame.Http404
	
# urls
urlPatterns = [
	("^/$", index),
	("^/count/([1-9]*)$", count),
]

# app running
app = frame.Frame(urlPatterns)
#app.testServer(80)