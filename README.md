# frame.py
frame.py is a web application framework for Python a la Django and web.py. It's nothing new, but gets things done the way I like them done.
It uses a regex driven URL to function mapping, jinja2 for templating, and wsgi for server communication.

## example with decorators
```python
from frame import Frame, Response, Http404

# initiate a Frame object
app = Frame()

# define a function to respond to a url, with its pattern in the decorator
@app.route("^/count/([1-9]*)$")
def count(request):
	if request.type == "GET":
		return Response("you entered " + str(request.capturedData.group(1)))
	else:
		raise Http404

# run the test server
app.testServer(80)
```

## example with pattern list
```python
from frame import Frame, Response, Http404

# define a function to respond to a url
def count(request):
	if request.type == "GET":
		return Response("you entered " + str(request.capturedData.group(1)))
	else:
		raise Http404

# define a pattern to map to that function	
urlPatterns = [
	("^/count/([1-9]*)$", count),
]

# initiate a Frame object and run the test server
app = Frame(urlPatterns)
app.testServer(80)
```