#Run the server
from flask import Flask, request
from flask_defs import get_username

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello():
    print('Hello, World!')
    return 'Hello, World!'

@app.route('/user', methods=['POST','GET'])
def user():
    print('Getting username...')
    return get_username()


if __name__ == "__main__":
    app.run(debug=True)
    pass