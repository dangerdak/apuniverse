from django.test import TestCase
from django.utils import timezone

from blog.models import Post


class PostTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            title='First Post',
            text='I like to boogie.',
            pub_date=timezone.now())

    def test_create_post(self):
        # Save post
        self.post1.save()

        # Check post can be retrieved
        all_posts = Post.objects.all()
        # Only one post should have been made
        self.assertEqual(len(all_posts), 1)
        # Created post should equal saved post
        only_post = all_posts[0]
        self.assertEqual(only_post, self.post1)

        # Check attributes
        self.assertEqual(only_post.title, 'First Post')
        self.assertEqual(only_post.text, 'I like to boogie.')
        self.assertEqual(only_post.pub_date.day, self.post1.pub_date.day)
        self.assertEqual(only_post.pub_date.month, self.post1.pub_date.month)
        self.assertEqual(only_post.pub_date.year, self.post1.pub_date.year)
        self.assertEqual(only_post.pub_date.hour, self.post1.pub_date.hour)
        self.assertEqual(only_post.pub_date.minute, self.post1.pub_date.minute)
        self.assertEqual(only_post.pub_date.second, self.post1.pub_date.second)
