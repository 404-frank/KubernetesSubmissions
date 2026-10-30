import socket, datetime
import os
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from nats.aio.client import Client as NATS
import asyncio
import globals

HOST = os.environ.get('BACKEND_SERVER_LISTENING_URL', '')
PORT = int(os.environ.get('BACKEND_SERVER_LISTENING_PORT', '3001'))
# TODO move to ENV var in config map:
NATS_URL = os.environ.get('NATS_URL', 'nats://my-nats:4222')
NATS_TODO_QUEUE = os.environ.get('NATS_TODO_QUEUE', 'distribute')
DISTRUBUTE_MESSAGE = eval(os.environ.get('DISTRUBUTE_MESSAGE', "True"))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        content_type = self.headers.get('Content-Type', 'text/html')
        if self.path == '/':
            print(f"got a connection on {self.path}")
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("200 OK"))
        elif self.path == '/healthz':
            print(f"got a connection on {self.path}, health check")
            database_healthy = globals.check_database_health()
            self.send_response(200 if database_healthy else 500)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("200 OK" if database_healthy else "500 NOT OK"))
        elif self.path == '/todos':
            print(f"got a GET connection on {self.path}")
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            body = globals.get_todos()
            self.wfile.write(self.create_response(body))
        else:
            self.send_response(404)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    def do_PUT(self):
        if self.path.startswith('/todos'):
            print(f"got a connection on {self.path}")
            todo_id = self.path.split("/")[-1]
            globals.set_todo_done(todo_id)
            self.send_response(200)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(self.create_response(f"todo with id {todo_id} was set to False"))
            if DISTRUBUTE_MESSAGE:
                # send todoRecord to distributor
                asyncio.run(self.distributeMessage({'entry_date': datetime.datetime.now(), 'title': "entry was set to done", 'id': todo_id, 'done': True}))

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin' , '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(SimpleHTTPRequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


    def do_POST(self):
        if self.path == '/todos':
            print(f"got a POST connection on {self.path}")
            content_length = int(self.headers.get('Content-Length', 0))
            content_type = self.headers.get('Content-Type', 0)
            post_data = self.rfile.read(content_length).decode('UTF-8')
            print(f"todo_message_posted : {post_data}")
            todo = json.loads(post_data)['todo']
            if len(todo) > 140:
                self.send_response(413)
                self.send_header('Content-type', "text/html")
                self.end_headers()
                print(f"ERROR, content length is larger than 140 characters, content: {todo}")
                self.wfile.write(self.create_response("ERROR, content length is larger than 140 characters"))
            else:
                todoRecord = globals.add_todo(todo)
                self.send_response(200)
                self.send_header('Content-type', "text/html")
                self.end_headers()
                self.wfile.write(self.create_response("ok"))
                if DISTRUBUTE_MESSAGE:
                    # send todoRecord to distributor
                    asyncio.run(self.distributeMessage(todoRecord))
                
        else:
            self.send_response(404)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(self.create_response("path not found"))

    async def distributeMessage(self, msg) -> None:
        if msg["entry_date"]:
            dtm = msg["entry_date"].strftime("%Y%m%d, %H:%M:%S")
            msg["entry_date"] = dtm
        cleanupMessage = self.removeFromJson(msg, "_id", "done")
        print(f"sending message: {msg}")
        nc = NATS()
        await nc.connect(servers=[NATS_URL])
        # await confirm_connection()
        await nc.publish(NATS_TODO_QUEUE, json.dumps(msg).encode())
        print("message has been sent")

    def removeFromJson(self, msg: json, *elements: str) -> json:
        for e in elements:
            if e in msg:
                msg.pop(e)
        return msg


    def create_response(self, body :str) -> bytes:
        response = f"{body}"
        return response.encode()


httpd = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
