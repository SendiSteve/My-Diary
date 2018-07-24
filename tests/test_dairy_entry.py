import json
from tests.base import BaseTestCase


class EntryTestCase(BaseTestCase):
    """Handles user entry test case"""

    def test_add_entry_successfully(self):
        """Test entry can be created successfully through the api"""

        with self.client:
            response = self.add_entry('Meeting with students')

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is created with 201 status code
            self.assertEqual(response.status_code, 201)
            self.assertEqual(expected.get('message'),
                             'Entry has been successfully recorded.')

    def test_entry_cannot_be_created_twice(self):
        """Test entry cannot be created twice through the api"""
        with self.client:
            response = self.add_entry('Meeting with students')

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is bad request with 400 status code
            self.assertEqual(response.status_code, 400)
            self.assertEqual(expected.get('message'),
                             'Entry with that name already recorded.')


    def test_entry_contains_atleast_5_characters(self):
        """Test entry title cannot have less than 5 characters"""
        with self.client:
            response = self.add_entry("met")

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is bad request with 400 status code
            self.assertEqual(response.status_code, 400)
            self.assertEqual(expected.get('message'),
                             'Title should be at least 5 characters long.')
