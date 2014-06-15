import os

from django.test import LiveServerTestCase
from django.test.client import Client
from django.utils import timezone

from blog.models import Post


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

    def test_create_post(self):
        # Log in
        self.client.login(username=os.environ['TESTUSER'],
                          password=os.environ['TESTUSERPASSWD'])
        # Check response code
        response = self.client.get('/admin/blog/post/add/')
        self.assertEqual(response.status_code, 200)

        # Create a new post
        response = self.client.post('/admin/blog/post/add/', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04'
            },
            follow=True
            )
        self.assertEqual(response.status_code, 200)

        # Check post was added successfully
        self.assertTrue(bytes('added successfully',
                              'UTF-8') in response.content)

        # Check new post is in database
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)

    def test_edit_post(self):
        # Create the post
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        post.save()
        ### Unnecessary
        # Check new post is in database
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post.title, 'My first post')
        self.assertEqual(only_post.text, 'This is my first blog post')
        ####

        # Log in
        self.client.login(username=os.environ['TESTUSER'],
                          password=os.environ['TESTUSERPASSWD'])
        ### Unnecessary
        # Check response code
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        # After logging in, page should contain 'Log out' string
        self.assertTrue(bytes('Log out', 'UTF-8') in response.content)

        # Check response code
        response = self.client.get('/admin/blog/post/1/')
        self.assertEqual(response.status_code, 200)
        ####

        # Edit the post
        response = self.client.post('/admin/blog/post/1/', {
            'title': 'My second post',
            'text': 'This is my second post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04'
            },
            follow=True
            )
        self.assertEqual(response.status_code, 200)

        # Check post was added successfully
        self.assertTrue(bytes('changed successfully', 'UTF-8') in response.content)

        # Check new post is in database
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEqual(only_post.title, 'My second post')
        self.assertEqual(only_post.text, 'This is my second post')

    def test_delete_post(self):
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        post.save()

        # Check that post is saved
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)

        # Log in
        self.client.login(username=os.environ['TESTUSER'],
                          password=os.environ['TESTUSERPASSWD'])

        # Delete the post
        response = self.client.post('/admin/blog/post/1/delete/', {
            'post': 'yes'
            },
            )
        self.assertEqual(response.status_code, 200)
        # Check are you sure is in loaded content
        self.assertTrue(bytes('you sure?', 'UTF-8') in response.content)

        # Check deleted successfully
        self.assertTrue(bytes('deleted successfully') in response.content)

        # Check removed from database
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 0)
