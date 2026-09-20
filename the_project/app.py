from flask import Flask
import views
import os

# print startup info
listening_url = os.environ.get('SERVER_LISTENING_URL', '0.0.0.0')
listening_port = os.environ.get('SERVER_LISTENING_PORT', '3000')
print(f"Flask server is starting, listening on port: [{listening_url}:{listening_port}]")


app = Flask(__name__)
app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host=listening_url, port=listening_port)
