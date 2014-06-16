from django.test import Client, LiveServerTestCase
from django.utils import timezone

from blog.models import Post


class PostViewTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        post = Post()
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.pub_date = timezone.now()
        post.save()

        # Check that the new post is in the database
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 1)

        # Fetch the index
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        # Check response contains correct info
        self.assertTrue(bytes(post.title, 'UTF-8') in response.content)
        self.assertTrue(bytes(post.text, 'UTF-8') in response.content)

        self.assertTrue(
            bytes(str(post.pub_date.year), 'UTF-8') in response.content)
        self.assertTrue(
            bytes(post.pub_date.strftime('%b'), 'UTF-8') in response.content)
        self.assertTrue(
            bytes(str(post.pub_date.day), 'UTF-8') in response.content)
