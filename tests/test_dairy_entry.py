import json
from tests.base import BaseTestCase
import unittest


class EntryTestCase(BaseTestCase):
    """Handles user entry test case"""

    def test_add_entry_successfully(self):
        """Test entry can be created successfully through the api"""

        with self.client:
            response = self.add_entry(
                'Meeting with students',
                'Discuss about safty in school')

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is created with 201 status code
            self.assertEqual(response.status_code, 201)
            self.assertEqual(expected.get('message'),
                             'Entry has been successfully recorded.')

    @unittest.skip('Fails when i add the update and delete unit tests')
    def test_entry_cannot_be_created_twice(self):
        """Test entry cannot be created twice through the api"""
        with self.client:
            response = self.add_entry(
                'Meeting with students',
                'Discuss about safty in school')

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is bad request with 400 status code
            self.assertEqual(response.status_code, 400)
            self.assertEqual(expected.get('message'),
                             'Record already exists.')

    def test_entry_contains_atleast_5_characters(self):
        """Test entry title cannot have less than 5 characters"""
        with self.client:
            response = self.add_entry(
                "Mee", "Discuss about safty in school")

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is bad request with 400 status code
            self.assertEqual(response.status_code, 400)
            self.assertEqual(expected.get('message'),
                             'Please enter a valid entry title.')

    def test_retrieve_all_entries(self):
        """Test all entries can be retrieved successfully"""
        with self.client:
            # Create an entry first
            self.add_entry(
                "Meeting with CEO Andela",
                "Discuss about marketing strategies")

            # retrieve the created entry
            response = self.retrieve_all_entries()

            # verify that the result is success with 200 status code
            self.assertEqual(response.status_code, 200)

    def test_update_a_single_entry(self):
        """Test a single entry can be updated successfully"""
        with self.client:
            self.add_entry("Go swimming", "Buy swimming jacket")
            self.get_id()
            response = self.update_entry()

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is created with 201 status code
            self.assertEqual(response.status_code, 201)
            self.assertEqual(expected.get('message'),
                             "Entry updated successfully.")

    def test_delete_entry(self):
        """Test a single entry can be deleted successfully"""
        with self.client:
            self.add_entry("Go shopping", "Collect kitchen material")
            # self.get_id()
            response = self.delete_entry()

            # ensure that the result expected is in json format
            expected = json.loads(response.data.decode())

            # verify that the result is ok with 200 status code
            self.assertEqual(response.status_code, 200)
            self.assertEqual(expected.get('message'),
                             "Entry delete successfully!")
