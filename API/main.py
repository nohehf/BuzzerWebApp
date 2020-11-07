#Run the server
from flask import Flask, jsonify, request, abort, Response, make_response
import json
from flask_defs import get_username

app = Flask(__name__)

playerList = []

@app.route('/login', methods=['POST'])
def login():
    playerString = request.data.decode("utf-8")
    playerJson = json.loads(playerString)
    print(playerJson['name'] + ' LOGGED IN')
    response = make_response("POST SUCCES", 200)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/buzzer', methods=['POST'])
def user():
    print('Getting username...')
    response = make_response('POST Response',200)
    response.mimetype = "text/plain"
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
    pass