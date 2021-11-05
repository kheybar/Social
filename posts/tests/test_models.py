# در زمان تست کردن مدل ها، ما کار زیادی با خود مدل کاری نداریم، بیش تر متود ها رو تست می‌کنیم

from django.test import TestCase
from posts.models import Post
from django.contrib.auth.models import User



class TestPost(TestCase):
    def setUp(self):
        user = User.objects.create(username='boss', email='boss@gmail.com', password='123456')
        self.post = Post.objects.create(
            user = user,
            body = 'This is a Test',
        )
    
    def test_post(self):
        self.assertEqual(self.post.slug, 'this-is-a-test')