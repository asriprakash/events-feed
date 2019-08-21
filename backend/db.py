from google.cloud import firestore
# from flask import abort
import datetime

EVENTS = firestore.Client().collection('events')


def add_events(id):
    print('adding a new event' + id + ' to firestore')
    doc_ref = EVENTS.document(id)
    doc_ref.set({
        u'eventDesc': u'Dummy',
        u'eventName': u'Lovelace'
    })
    print ("success")
    return id
