import socket
import os
import globals

HOST = ""  # Standard loopback interface address (localhost)
PORT = 5100  # Port to listen on (non-privileged ports are > 1023)

def build_response(status_code, body, content_type='text/html'):
    # Build the HTTP response
    status_line = f"HTTP/1.1 {status_code}\r\n"
    headers = f"Content-Type: {content_type}\r\nContent-Length: {len(body)}\r\n"
    response = f"{status_line}{headers}\r\n{body}"
    return response.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"server is listening on port {PORT}" )
    while True:
       conn, addr = s.accept()
       print(f"got a connection from {addr}")
       ping_pong_counter = globals.get_counter() + 1
       output_string = "ping pong, counter: <br /><br />" + str(ping_pong_counter)
       conn.sendall(build_response(200, output_string))
       conn.close()
       globals.set_counter(ping_pong_counter)
