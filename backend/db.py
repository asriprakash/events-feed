from google.cloud import firestore
# from flask import abort
import datetime

EVENTS = firestore.Client().collection('events')


def add_events_test(id):
    print('adding a new event' + id + ' to firestore')
    doc_ref = EVENTS.document(id)
    doc_ref.set({
        u'eventDesc': u'Dummy',
        u'eventName': u'Test',
        u'eventsDate': u'8/12/2019',
    })
    print ("success")
    return id


def add_events(data, id):
    print('adding a new event' + id + ' to firestore')
# data['eventDate'] = datetime.datetime.now()
    EVENTS.document(id).set(data)
    return id


def get_events():
    print('Retrieving events from firestore')
    docs = EVENTS.order_by('eventDate', direction=firestore.Query.DESCENDING).get()
    ret = []
    for doc in docs:
        d = doc.to_dict()
        d['id'] = doc.id
        ret.append(d)
    return ret
