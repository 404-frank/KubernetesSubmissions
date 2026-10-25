from flask import Flask, jsonify, render_template
import views
import os

# print startup info
listening_url = os.environ.get('SERVER_LISTENING_URL', '0.0.0.0')
listening_port = os.environ.get('SERVER_LISTENING_PORT', '3000')
print(f"Flask server is starting, listening on port: [{listening_url}:{listening_port}]")

healthy = True

app = Flask(__name__)

# health handling
@app.route('/healthz')
def healthz():
    print(f"healthy: {healthy}")
    if healthy:
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"status": "not ok"}), 500

# separate fail method to be able to 'touch' the flask app
@app.route('/fail', methods=['GET', 'POST'])
def fail():
    global healthy
    healthy = False
    return render_template('failure.html')

app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST', 'PUT'])

if __name__ == '__main__':
    app.run(host=listening_url, port=listening_port)
