import json
import unittest
from app import app, app_config


ENTRIES = []


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
         Create an instance of the app with the testing configurations
        """
        app.config.from_object(app_config['testing'])
        return app

    def setUp(self):
        """Runs its code before every single test"""
        # Initialize the test client
        self.client = app.test_client(self)

    def tearDown(self):
        """Drop any stored data in the list after every single test runs"""
        ENTRIES[:] = []

    def add_entry(self, title, notes):
        """This method adds an entry"""
        return self.client.post(
            'api/v1/user/entries',
            data=json.dumps(
                dict(
                    title=title,
                    notest=notes
                )), content_type='application/json')
