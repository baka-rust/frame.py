from frame import Frame, Http404, Redirect
 
app = Frame()
 
@app.route("^/$")
def index(request):
	return "hello world."
	
@app.route("^/count/([1-9]*)$")
def count(request):
	if request.type == "GET":
		return "you entered " + str(request.capturedData)
	else:
		raise Http404

#app.testServer(666)