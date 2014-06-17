# frame.py
frame.py is a web application framework for Python a la Django and web.py. It's nothing new, but gets things done the way I like them done.
It uses a regex driven URL to function mapping, and wsgi for server communication.

## example with decorators
```python
from frame import Frame, Response, Http404

# initiate a Frame object
app = Frame()

# define a function to respond to a url, with its pattern in the decorator
@app.route("^/count/([1-9]*)$")
def count(request):
	if request.type == "GET":
		return Response("you entered " + str(request.matchObject.group(1)))
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
		return Response("you entered " + str(request.matchObject.group(1)))
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

## deploying with google app engine
Because frame.py uses WSGI, it is quite easy to set it up with the Google App Engine.
Simply create a new file in your project directory called *wsgi.py* or something to that effect. Inside, include:
```python
# make sure {frameApp} actually matches the name of your application
from frameApp import app
application = app.application
```
Then, modify your *app.yaml* to include:
```yaml
handlers:
- url: .*
  script: wsgi.application
```
If you would like to have app engine handle static files (recommended), modify your *app.yaml* to include (before the script handler):
```yaml
handlers:
- url: /static
  static_dir: static
```
And then change your frame.py application initialization to not serve static files.
```python
app = Frame(staticDir=None)
```