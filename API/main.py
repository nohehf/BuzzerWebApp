#Run the server
from flask import Flask, request
app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello():
    print('Hello, World!')
    return 'Hello, World!'

@app.route('/user', methods=['POST','GET'])
def get_username():
    if request.method == 'POST':
        print('POST')
        username = request.form['username']
        print(username)
    if request.method == 'GET':
        print('GET')
        username = request.form['username']
        print(username)
    return username


if __name__ == "__main__":
    app.run(debug=True)
    pass