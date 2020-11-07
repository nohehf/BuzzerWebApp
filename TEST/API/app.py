# https://medium.com/swlh/implement-a-websocket-using-flask-and-socket-io-python-76afa5bbeae1 SOURCE
from flask import Flask, jsonify, request, abort, Response, make_response, render_template
from flask_socketio import SocketIO
async_mode = None
import json

app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode)

playerList =[]
@app.route('/')
def index():
    return render_template('index.html',sync_mode=socket_.async_mode)

@socket_.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})

if __name__ == "__main__":
    socket_.run(app,debug=True)
    pass