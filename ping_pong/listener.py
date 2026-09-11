from http.server import HTTPServer, BaseHTTPRequestHandler
import globals

HOST = ""  # Standard loopback interface address (localhost)
PORT = 5100  # Port to listen on (non-privileged ports are > 1023)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        content_type = self.headers.get('Content-Type', 'text/html')
        if self.path == '/pingpong':
            print(f"got a connection from {self.path}")
            ping_pong_counter = globals.get_counter() + 1
            globals.set_counter(ping_pong_counter)
            body = "ping pong, counter: <br /><br />" + str(ping_pong_counter)
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            print(f"calling create_response with this param: [{body}]")
            self.wfile.write(self.create_response(body))
        elif self.path == '/pings':
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response(str(globals.get_counter())))
        else:
            self.send_response(404)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    def create_response(self, body :str) -> bytes:
        response = f"{body}"
        return response.encode()


httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
