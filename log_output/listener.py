from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import globals

HOST = ""  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)
PINGS_URL = 'http://127.0.0.1:5100/pings'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        content_type = self.headers.get('Content-Type', 'text/html')
        if self.path == '/log':
            print(f"got a connection on {self.path}")
            pingpong_counter = self.get_counter()
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            body = f"{globals.get_stamp()} <br /><br />Ping / Pongs: {pingpong_counter}"
            self.wfile.write(self.create_response(body))
        else:
            self.send_response(404)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    def get_counter(self) -> str:
        req = requests.get(PINGS_URL)
        return req.content.decode("UTF-8")

    def create_response(self, body :str) -> bytes:
        response = f"{body}"
        return response.encode()


httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
