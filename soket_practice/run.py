import os
from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit, send
import json


# https://yumere.tistory.com/53

app = Flask(__name__)
app.config["SECRET_KEY"] = "KEY"
app.config['JSON_AS_ASCII'] = False
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET','POST']):
    print('message was received!!!')

@socketio.on('my event')
def hadle_my_custom_event(req, methods=['GET', 'POST']):
    print('received my event: ' + str(req))
    if req.get('message') is not None:
        mes = req.get('message')
        print(mes)

    emit('my response', req, callback=messageReceived)

if __name__ == "__main__":
    socketio.run(app, debug=True)