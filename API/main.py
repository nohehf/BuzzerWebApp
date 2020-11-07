#Run the server
from flask import Flask, jsonify, request, abort, Response, make_response
import json
from flask_defs import get_username
import pathlib
import os
import sys

current_path = os.getcwd() #On setup le bon path pour être sur d'avoir les modules de bien importés, peut n'importe l'interpréteur.
split = current_path.split('\\')
if split[-1] != 'BuzzerWebApp':
    split.pop()
    BuzzerWebApp_folder_path = '\\'.join(split)
    sys.path.append(BuzzerWebApp_folder_path)

from player import Player

path = str(pathlib.Path(__file__).parent.parent.absolute()) + r'\yourLocalUrl.txt'
print(path)
urlFile = open(path,'r')
myUrl = urlFile.read()
urlFile.close()

app = Flask(__name__)

playerList = {}

@app.route('/login', methods=['POST'])
def login():
    playerString = request.data.decode("utf-8") #On récupere la data de la requete sous forme de string
    playerJson = json.loads(playerString) #on la transforme en json
    player = Player(playerJson['name']) #on crée un nouveau joueur
    print(player.name + ' LOGGED IN') 
    response = make_response("POST SUCCES", 200)
    response.headers["Access-Control-Allow-Origin"] = "*" 
    playerList[player.name] = player #On ajoute le joueur à la playerList, pour le moment on identifie par name, il faudra plus tard associer un id
    return response

@app.route('/buzzer', methods=['POST'])
def user():
    dataString = request.data.decode("utf-8")
    dataJson = json.loads(dataString)
    name = dataJson['name'] #On récupere le nom du joueur qui à buzzé
    player = playerList[name] #on cherche le player correspondant dans playerList
    player.buzz() #on appelle la méthode buzz pour le joueur qui à buzzé
    response = make_response("POST SUCCES", 200)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response



if __name__ == "__main__":
    app.run(debug=True,host=myUrl)
    pass