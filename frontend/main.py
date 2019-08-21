from flask import Flask, render_template, request, redirect, abort, jsonify
import requests
# from datetime import datetime
# import re
import os
import uuid
# import auth
# import json
# from collections import namedtuple
try:
    import googleclouddebugger
    googleclouddebugger.enable()
except ImportError:
    pass

app = Flask(__name__)

try:
    app.config.from_object(os.environ['APP_SETTINGS'])
    URL = app.config['API']
    BUCKET = app.config['BUCKET']
    PROJECT_NAME = app.config['PROJECT']
except:
    URL = 'http://35.236.255.242:8080'
    PROJECT_NAME = 'events-feed-deloitte'

# @app.route("/")
# def home():
#   try:
#     data =  requests.get(URL + '/events').content
#     # Parse JSON into a python object with attributes corresponding to dict keys.
#     model = { 'events': json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))} 
#   except Exception: 
#     # backend is down, so provide alternative data
#     model = {}
#   model['greeting'] = os.getenv('GREETING', 'Welcome to Events feed')
#   return render_template("home.html", model=model, bucket=BUCKET)


@app.route("/")
def showEvents():
    return render_template("login.html")


@app.route("/addEvent")
def addEvent():
    return render_template("createEvent.html")


@app.route("/events/add", methods=['POST'])
def add_event():
    print('URL--' + URL)
    url = 'http://35.236.255.242:8080' + '/events/add/' + str(uuid.uuid4())
    data = request.form.to_dict(flat=True)
    print(requests.post(url, data=data))
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)
