from flask import Flask

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello():
    print('Hello, World!')
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)