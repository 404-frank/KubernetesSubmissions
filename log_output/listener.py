from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import globals
import os

HOST = ""  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)
PINGS_URL = 'http://127.0.0.1:5100/pings'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        content_type = self.headers.get('Content-Type', 'text/html')
        if self.path == '/log':
            print(f"got a connection on {self.path}")
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            file_content = globals.get_file_content("shared/information.txt")
            print(f"file_content: {file_content}")
            env_variabele = f"env variabele: message={os.environ['message']}"
            print(f"env_variabele: {env_variabele}")
            pingpong_counter = self.get_counter()
            body = f"{file_content}<br />{env_variabele}<br />{globals.get_stamp()}<br />Ping / Pongs: {pingpong_counter}"
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
