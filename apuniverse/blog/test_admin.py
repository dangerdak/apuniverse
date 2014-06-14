import os

from django.test import LiveServerTestCase, Client


class AdminTest(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        # Create client
        self.client = Client()

    def test_login(self):
        # Get login page
        response = self.client.get('/admin/')

        # Check response code
        self.assertEqual(response.status_code, 200)
        # Initial page should contain 'Log in' string
        self.assertTrue(bytes('Log in', 'UTF-8') in response.content)

        # Log in
        self.client.login(username=os.environ['TESTUSER'],
                          password=os.environ['TESTUSERPASSWD'])

        # Check response code
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        # After logging in, page should contain 'Log out' string
        self.assertTrue(bytes('Log out', 'UTF-8') in response.content)

    def test_logout(self):
        # Log in
        self.client.login(username=os.environ['TESTUSER'],
                          password=os.environ['TESTUSERPASSWD'])

        # Check response code
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        # After logging in, page should contain 'Log out' string
        self.assertTrue(bytes('Log out', 'UTF-8') in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        # Logged out page should contain 'Log in' string
        self.assertTrue(bytes('Log in', 'UTF-8') in response.content)
