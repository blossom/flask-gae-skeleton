# -*- coding: utf-8 -*-
import unittest
from main import app

class TestStaticPages(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_landing_index(self):
        "Should have an index for the landing page with a welcome message"
        response = self.client.get('/')
        print response.data
        assert 'we will inform you as soon as' in response.data

if __name__ == '__main__':
    unittest.main()
