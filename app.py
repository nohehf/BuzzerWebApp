from flask import Flask, jsonify, abort, Response, make_response, render_template, session, copy_current_request_context , request
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from lib.player import Player

#IMPORT CONFIG FILE:
from configparser import ConfigParser
config = ConfigParser()
config.read("config.ini")


#SERVER CONFIG
host = config["SERVER"]['host']
port = config["SERVER"]['port']

# Flask and Socket-IO setup
async_mode = None
app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode)

#This might work with different settings
thread = None
thread_lock = Lock()

playerList = {} #We create a dictionnary to store Players objects, with playerName as dict key

@app.route('/') #Simply render the main page on root url
def index():
    return render_template('index.html',sync_mode=socket_.async_mode)

@socket_.on('login', namespace='/test') #Name space has to be changed
def connect_message(message):
    print(message)
    playerName = message['name']
    playerSid = request.sid
    player = Player(playerName,playerSid) #Creates a new Player instance
    playerList[message['name']] = player #Save it into the dictionnary
    emit('loginResponse', {'data': "Logged as : " + playerName + "<br> Your Sid=" + playerSid})
    print(playerList)



@socket_.on('buzz',namespace='/test') 
def buzz(message):
    playerThatBuzzed = playerList[message['name']] #Retrives the Player objects associated with the name of the player that buzzed
    print('Player : ' + playerThatBuzzed.name + ' buzzed !')
    emit('buzzResponse', {'data': playerThatBuzzed.name}, broadcast=True) #Send back the name of the player that buzzed to all players
    config.read('config.ini') #We update the config before next step (because confing can be modified while server running) 
    playerThatBuzzed.buzz(config) #We trigger the buzz method of Player and pass the config to it (for the discord webhook to access it)



if __name__ == "__main__":
    socket_.run(app,debug=True,host=host,port=port)
    pass





