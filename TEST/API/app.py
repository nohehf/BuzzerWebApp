# https://medium.com/swlh/implement-a-websocket-using-flask-and-socket-io-python-76afa5bbeae1 SOURCE

# https://stackoverflow.com/questions/53807546/concise-example-of-how-to-join-and-leave-rooms-using-flask-and-socket-io ROOMS

from flask import Flask, jsonify, abort, Response, make_response, render_template, session, copy_current_request_context , request
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
async_mode = None
import json

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

playerList ={}  #Associe discord name et Sid

@app.route('/')
def index():
    return render_template('index.html',sync_mode=socket_.async_mode)

@socket_.on('login', namespace='/test')
def connect_message(message):
    print(message)
    # session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response', {'data': "Logged as : " + message['name'] + "<br> Your Sid=" + request.sid})
    playerList[message['name']] = request.sid
    print(playerList)

@socket_.on('buzz',namespace='/test')
def buzz(message):
    responseMessage = 'Player: ' + message['name'] + ' Buzzed'
    print('BUZZ!!')
    print(responseMessage)
    emit('response', {'data': message['name']}, broadcast=True)
    


@socket_.on('my_event', namespace='/test')
def test_message(message):
    print(message)
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('response',
         {'data': message['data'], 'count': session['receive_count']})
    testEmit()

def testEmit():
    emit('my_response', {'data':'FONCTION TEST EMIT'})


if __name__ == "__main__":
    socket_.run(app,debug=True,host="192.168.1.167")
    pass