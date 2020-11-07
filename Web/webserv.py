from flask import Flask, render_template
import os
import pathlib

app = Flask(__name__)

path = str(pathlib.Path(__file__).parent.parent.absolute()) + r'\yourLocalUrl.txt'
print(path)
urlFile = open(path,'r')
myUrl = urlFile.read()
urlFile.close()

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host=myUrl, port=80)
    pass