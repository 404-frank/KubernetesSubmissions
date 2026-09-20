import socket
import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import globals

HOST = os.environ.get('BACKEND_SERVER_LISTENING_URL', '')
PORT = int(os.environ.get('BACKEND_SERVER_LISTENING_PORT', '3000'))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        content_type = self.headers.get('Content-Type', 'text/html')
        if self.path == '/todos':
            print(f"got a GET connection on {self.path}")
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            body = f"{globals.get_todos()}"
            self.wfile.write(self.create_response(body))
        else:
            self.send_response(404)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin' , '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control'                , 'no-store, no-cache, must-revalidate')
        return super(SimpleHTTPRequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


    def do_POST(self):
        if self.path == '/todos':
            print(f"got a POST connection on {self.path}")

            content_length = int(self.headers.get('Content-Length', 0))
            content_type = self.headers.get('Content-Type', 0)
            print(f"content length: {content_length}")
            print(f"content type: {content_type}")
            post_data = self.rfile.read(content_length).decode('UTF-8')
            print(f"post_data : {post_data}")
            todo = json.loads(post_data)['todo']
            globals.add_todo(todo)
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(self.create_response("ok"))
        else:
            self.send_response(404)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    def create_response(self, body :str) -> bytes:
        response = f"{body}"
        return response.encode()


httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
