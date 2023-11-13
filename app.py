import time
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
	return render_template('index.html')

@socketio.on('ping')
def handle_ping():
	msg = 'Sockets work!'
	socketio.emit('pong', msg)
	for i in range(len(msg)):
		time.sleep(0.2)
		socketio.emit('colored', i)

if __name__ == '__main__':
	socketio.run(app)