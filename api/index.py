# A custom request handler class handler is created by inheriting from BaseHTTPRequestHandler. 
# This class will define how the server responds to HTTP requests.
# This basic server will respond to any GET request with "Hello, world!".
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
# This method handles GET requests. 
# When a GET request is received, this method is automatically called.
    def do_GET(self):
        # Sends a 200 OK response status code to indicate the request was successful.
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('class handler(BaseHTTPRequestHandler):'.encode('utf-8'))
        return

