from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_str(self):
        post = Post.objects.create(title='X', content='Y')
        self.assertEqual(str(post), 'X')

