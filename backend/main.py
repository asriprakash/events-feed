from flask import Flask
import db

app = Flask(__name__)


@app.route('/')
def default_events():
    return "hello world"


@app.route('/events/add/<id>', methods=['POST'])
def add_events():
    event = db.add_events()
    return event


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
