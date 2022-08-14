from flask import Flask, jsonify, render_template,request, Response
import requests
import json
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.secret_key = "andh346isname3467356isj356621ohnce9980na"
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template('ChatApp.html')

# # Send message
def messageRecived():
  print( 'message was received!!!' )


# # Listen to event
@socketio.on ('my event')
def handle_my_custom_event( json ):
    print( 'received something', str(json))
    socketio.emit('my response', json)

if __name__ == "__main__":
    socketio.run(app,debug=True)