from flask import request


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