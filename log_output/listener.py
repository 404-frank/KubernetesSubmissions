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
        if self.path == '/':
            print(f"got a connection on {self.path}")
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("200 OK"))
        # health check
        if self.path == '/healthz':
            print(f"got a connection on {self.path}, health check")
            pingpong_healthy = self.ping_pong_health_check()
            self.send_response(200 if pingpong_healthy else 500)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("200 OK" if pingpong_healthy else "500 NOT OK"))
        elif self.path == '/log':
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
            print(f"in error catch: path {self.path}")
            self.send_response(404)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    # check if the response of get pings is integer
    def ping_pong_health_check(self) -> bool:
        try:
            int(self.get_counter())
        except ValueError:
            return False
        return True

    def get_counter(self) -> str:
        try:
            req = requests.get(PINGS_URL)
            return req.content.decode("UTF-8")
        except requests.exceptions.RequestException:
            return "ERROR"

    def create_response(self, body :str) -> bytes:
        response = f"{body}"
        return response.encode()


httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
