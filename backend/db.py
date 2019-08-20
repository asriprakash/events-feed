from google.cloud import firestore
# from flask import abort
import datetime

EVENTS = firestore.Client().collection('events')


def add_events():
    id = '10001'
    print('adding a new event' + id + ' to firestore')
    doc_ref = EVENTS.document(u'10001')
    doc_ref.set({
        u'eventDesc': u'Ada',
        u'eventDate': u'Lovelace'
    })
    print ("success")
    return id
