from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send_response() and end_headers() are mandatory,
        # otherwise the response wont be considered as valid.
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
    
    def do_POST(self):
        if self.path == "/webhook":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'this is a webhook response')
        else:https://github.com/r2123b/simplest-python-server
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'you typed the wrong URL')

server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()
