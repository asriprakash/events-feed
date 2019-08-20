from flask import Flask
import db

app = Flask(__name__)


@app.route('/')
def create_hero():
    # req = Flask.request.json
    event = db.add_events()
    return Flask.jsonify({'id': event}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)