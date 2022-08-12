from flask import Flask, jsonify, render_template,request, Response
# from connection1 import mydb
import requests
import json
from flask_socketio import SocketIO, send, emit

# mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key = "andhisnameisjohncena"
socketio = SocketIO(app)

@app.route("/")
def home():
    return "Hello There!!"



if __name__ == "__main__":
    socketio.run(app,debug=True)