from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework.authtoken.models import Token

class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('u','u@u.com','pwd')
        self.token = Token.objects.create(user=self.user)
        Post.objects.create(title='T1', content='C1')
    def test_list(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
    def test_create_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res = self.client.post('/api/posts/', {'title':'T2','content':'C2'})
        self.assertEqual(res.status_code, 201)
