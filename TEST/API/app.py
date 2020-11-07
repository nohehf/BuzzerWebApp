from flask import Flask, jsonify, request, abort, Response, make_response
import json

app = Flask(__name__)
playerList =[]
@app.route('/login', methods=['POST'])
def login():
    playerString = request.data.decode("utf-8")
    playerJson = json.loads(playerString)
    print(playerJson['name'] + ' LOGGED IN')
    response = make_response("jsonify(player)", 200)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == "__main__":
    app.run(debug=True)
    pass