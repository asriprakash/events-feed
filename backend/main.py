import flask
import db
import json

app = flask.Flask(__name__)


@app.route('/')
def default_events():
    return "hello world"


@app.route('/events/add/<id>', methods=['POST'])
def add_events(id):
    data = flask.request.form.to_dict(flat=True)
    event = db.add_events(data, id)
    return flask.jsonify({'id': event}), 201
    return event


@app.route('/events', methods=['POST'])
def get_events():
    print('backend service responding to request for events')
    # string is default to prevent error when jsonifying python datetime
    return json.dumps(db.get_events(), indent=4, sort_keys=True, default=str), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
