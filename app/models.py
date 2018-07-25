"""This handles all operations on the entry object"""
import datetime
import uuid
import json

from pytz import utc

ENTRIES = []


class Entry(object):
    """Represents the Entry object"""

    def __init__(self, title, notes):
        self.id = uuid.uuid4().hex
        self.title = title
        self.notes = notes
        self.date_created = datetime.datetime.now(utc)

    def json(self):
        """Representation of entry object in json format"""
        return json.dumps({
            'id': self.id,
            'title': self.title,
            'notes': self.notes,
            'date_created': self.date_created
        })

    def create_entry(self):
        """Adds an entry to ENTRIES list"""

        # create new entry object
        newEntry = Entry(self.title, self.notes)

        for entry in ENTRIES:
            if self.title == entry.title:
                return {
                    'message': 'Record already exists.',
                    'status': False
                }
        # append newEntry object to ENTRIES
        ENTRIES.append(newEntry)
        return {'message': 'Entry has been successfully recorded.',
                'status': True
                }
