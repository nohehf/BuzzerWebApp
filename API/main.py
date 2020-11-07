#Run the server
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route('/')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Recived POST request with :')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        print('Recived GET request')
        return 'OK',200



if __name__ == "__main__":
    app.run(debug=True)
    pass