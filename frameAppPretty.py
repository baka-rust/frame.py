from frame import Frame, Response, Http404, Redirect
 
app = Frame()
 
@app.route("^/$")
def index(request):
	return Response("hello world.")
	
@app.route("^/count/([1-9]*)$")
def count(request):
	if request.type == "GET":
		return Response("you entered " + str(request.capturedData.group(1)))
	else:
		raise Http404

#app.testServer(80)