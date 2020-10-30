import os
from flask import Flask, render_template, session
from flask_socketio import SocketIO, send
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "KEY"

# json에서 ascii값 받지 않음
app.config['JSON_AS_ASCII'] = False
# app.config["Access-Control-Allow-Origin"] = "*"
socketio = SocketIO(app=app, cors_allowed_origins='*')

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
    
    socketio.emit('my response', req, callback=messageReceived)

@socketio.on("draw")
def handle_draw_event(data, methods=['GET','POST']):
    # print("draw data : ", data)

    socketio.emit('draw response', data, callback=messageReceived)
# goolge 드라이브랑 연결
# 관련 유튜브
# 캐치마인드?
# 달력
if __name__ == "__main__":
    socketio.run(app, debug=True)