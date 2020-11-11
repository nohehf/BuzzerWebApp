#Run the server
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
port = int(config["SERVER"]['port'])

#On setup flask et SocketIO
async_mode = None
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
#A tester différemment:
thread = None
thread_lock = Lock()

playerList = {} #Associe discord name et Sid

@app.route('/')  #Login Peut etre accueil plus tard
def index():
    return render_template('index.html',sync_mode=socket_.async_mode)

@app.route('/buzz')  #Desormais l'index est host sur le meme serveur
def buzzPage():
    return render_template('buzz.html',sync_mode=socket_.async_mode)

@socket_.on('login', namespace='/test') #CHANGE NAMESPACE
def connect_message(message):
    print(message)
    playerName = message['name']
    playerSid = request.sid
    player = Player(playerName,playerSid) #On crée un nouveau joueur /!\ il va falloir vérifier l'unicité du nom et si il exite déja juste changer le sid
    playerList[message['name']] = player #On l'ajoute à la liste de joueurs.
    emit('loginResponse', {'data': "Logged as : " + playerName + "<br> Your Sid=" + playerSid})
    print(playerList)

@socket_.on('login_test',namespace='/test')
def newLogin(message):
    playerName = message['name']
    playerSid = request.sid
    player = Player(playerName,playerSid) #On crée un nouveau joueur /!\ il va falloir vérifier l'unicité du nom et si il exite déja juste changer le sid
    playerList[message['name']] = player #On l'ajoute à la liste de joueurs.
    emit('redirect', '/buzz')
    emit('loginResponse', {'data': "Logged as : " + playerName + "<br> Your Sid=" + playerSid})
    print(playerList)


@socket_.on('buzz',namespace='/test') 
def buzz(message):
    playerThatBuzzed = playerList[message['name']] #On récupere l'objet player associé au nom du joueur qui a buzzé
    print('BUZZ!!')
    emit('buzzResponse', {'data': playerThatBuzzed.name}, broadcast=True)
    config.read('config.ini')
    playerThatBuzzed.buzz(config)



if __name__ == "__main__":
    socket_.run(app,debug=True,host=host,port=port)
    pass

#======================      OLD       =================================
# @app.route('/login', methods=['POST'])
# def login():
#     playerString = request.data.decode("utf-8") #On récupere la data de la requete sous forme de string
#     playerJson = json.loads(playerString) #on la transforme en json
#     player = Player(playerJson['name']) #on crée un nouveau joueur
#     print(player.name + ' LOGGED IN') 
#     response = make_response("POST SUCCES", 200)
#     response.headers["Access-Control-Allow-Origin"] = "*" 
#     playerList[player.name] = player #On ajoute le joueur à la playerList, pour le moment on identifie par name, il faudra plus tard associer un id
#     return response

# @app.route('/buzzer', methods=['POST'])
# def user():
#     dataString = request.data.decode("utf-8")
#     dataJson = json.loads(dataString)
#     name = dataJson['name'] #On récupere le nom du joueur qui à buzzé
#     player = playerList[name] #on cherche le player correspondant dans playerList
#     player.buzz() #on appelle la méthode buzz pour le joueur qui à buzzé
#     response = make_response("POST SUCCES", 200)
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return response



