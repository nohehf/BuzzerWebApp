#Run the server
from flask import Flask, request
import flask
from flask_defs import get_username

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello():
    response = flask.make_response('Get Response',200)
    response.mimetype = "text/plain"
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/buzzer', methods=['POST'])
def user():
    print('Getting username...')
    response = flask.make_response('POST Response',200)
    response.mimetype = "text/plain"
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
    pass