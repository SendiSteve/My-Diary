"""This handles views for the entry"""

from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from app.models import Entry, ENTRIES


class EntryList(Resource):
    """Handles operations on an Entry"""

    def post(self):
        """Handles creation of a new diary entry"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            'title',
            type=str,
            required=True,
            help='Entry title required please!')

        parser.add_argument(
            'notes',
            type=str,
            required=True,
        )

        args = parser.parse_args()
        title = args['title']
        notes = args['notes']

        # create entry object here
        entry = Entry(title, notes)
        # Validate user entry
        if len(title.strip()) < 5:
            return make_response(jsonify(
                {'message': 'Please enter a valid entry title.'}), 400)

        # call method to create entry
        resp = entry.create_entry()
        if not resp['status']:
            return make_response(jsonify({
                "message": resp['message']
            }), 400)

        return make_response(jsonify({
            "message": resp['message']
        }), 201)

    def get(self):
        """Handles retrieval of all entries in a diary"""

        entries = []

        for entry in ENTRIES:
            entry_data = {
                "id": entry.id,
                "title": entry.title,
                "notes": entry.notes,
                "date_created": entry.date_created
            }
            entries.append(entry_data)
        return make_response(jsonify({"Entries": entries}), 200)


class EntryResource(Resource):
    """Handles operations on a single entry"""

    def put(self, entry_id):
        """Handles update of a single entry"""

        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('notes', type=str, required=True)

        for entry in ENTRIES:
            if entry.id == entry_id:
                args = parser.parse_args()
                if entry.title in ENTRIES:
                    return make_response(jsonify({
                        'message': 'Entry with that name already recorded.'}),
                        400)
                entry.title = args['title']
                entry.notes = args['notes']

                return make_response(jsonify(
                    {'message': 'Entry updated successfully.'}),
                    201)
        return make_response(jsonify(
            {'message': 'Entry with that ID not found'}),
            400)

    def get(self, entry_id):
        """Returns a single entry"""
        for entry in ENTRIES:
            if entry.id == entry_id:
                entry_data = {
                    "id": entry.id,
                    "title": entry.title,
                    "notes": entry.notes,
                    "date_created": entry.date_created
                }

                return make_response(jsonify({
                    'Entry': entry_data}), 200)
        return make_response(jsonify({
            'message': 'Entry with that id not found'}),

    def delete(self, entry_id):
        """Handles deletion of a single entry"""

        for entry in ENTRIES:
            if entry.id == entry_id:
                ENTRIES.remove(entry)

                return make_response(jsonify(
                    {'message': 'Entry delete successfully!'}), 200)

            return make_response(jsonify({
                'message': 'Entry with that id not found'}),
                400)
        return make_response(jsonify({
            'message': 'Entry not found'}),
            400)
