# frame.py
frame.py is a web application framework for Python a la Django and web.py. It's nothing new, but gets things done the way I like them done.
It uses a regex driven URL to function mapping, jinja2 for templating, and wsgi for server communication.

## example
```python
import frame

# define a function to respond to a url
def count(request):
	return "you entered " + str(request.capturedData)

# define a pattern to map to that function	
urlPatterns = [
	("^/count/([1-9]*)$", count),
]

# initiate a Frame object and run the test server
app = frame.Frame(urlPatterns)
app.testServer(80)
```