from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

# Test sprawdzający, czy użytkownik zalogowany może tworzyć bloga z tytułem i opisem
# Po wykonaniu testu zwraca 
# System check identified no issues (0 silenced).
# Ran 1 test in 0.157s
# OK
# Destroying test database for alias 'default'...

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):

    # Tworzenie użytkownika
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

    # Tworzenie nowego posta na blogu
        test_post = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')