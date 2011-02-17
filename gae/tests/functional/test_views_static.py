# -*- coding: utf-8 -*-
import os
import signal
from subprocess import Popen
from selenium.firefox.webdriver import WebDriver

import unittest

from main import app
import settings


class TestStaticPages(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index(self):
        "Should have an index page with a welcome message"
        response = self.client.get('/')
        assert 'Welcome to Flask-Gae-Skeleton!' in response.data

class TestStaticPagesWithJs(unittest.TestCase):

    def setUp(self):
        self.server = Popen("dev_appserver.py . --port=80", shell=True)
        self.browser = WebDriver()

    def tearDown(self):
        self.browser.quit()
        # same as in python2.6 subprocess for posix systems (so currently no windows support)
        os.kill(self.server.pid, signal.SIGTERM)

    def test_index_with_js(self):
        self.browser.get('http://localhost')
        assert 'Welcome to Flask-Gae-Skeleton!' in self.browser.get_page_source()
