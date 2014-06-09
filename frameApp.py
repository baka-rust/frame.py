import frame

# views
def index(request):
	return "hello world." # call frame.render on template here
	
def count(request):
	return "you entered " + str(request.capturedData)
	
# urls
urlPatterns = [
	("^/$", index),
	("^/count/([1-9]*)$", count),
]

# app running
app = frame.Frame(urlPatterns)
app.testServer(80)