from flask import Flask, render_template
import os

# template_dir = os.path.abspath('web')
# print(template_dir)
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,host='192.168.1.167', port=80)
    pass