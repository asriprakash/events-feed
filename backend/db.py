from google.cloud import firestore
# from flask import abort
import datetime

EVENTS = firestore.Client().collection('events')


def add_events():
    data = []
    id = '10001'
    print('adding a new event' + id + ' to firestore')
    # data['eventDate'] = datetime.datetime.now()
    # data['eventName'] = 'Test Event'
    # data['eventDesc'] = 'test description'
    data[0] = 'hi'
    print (data)
    EVENTS.document(id).set(data)
    return id
