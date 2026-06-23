from flask import Flask
import views
import os

# print startup info
listen_on = os.environ.get('LISTENING_PORT', 'NOT FOUND')
print(f"Flask server is starting, listening on port: [{listen_on}]")


app = Flask(__name__)
app.add_url_rule('/', view_func=views.index)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=listen_on)
