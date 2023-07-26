from django.test import TestCase #let's us create sample database
from .models import Post 
from django.urls import reverse

# Create your tests here.
# start all test func names with "test_something".

class PostModelTest(TestCase):
    def setUp(self):
        '''created a new database with one entry'''
        Post.objects.create(text='just a text')

    def test_text_content(self):
        '''test'''
        post = Post.objects.get(id=1) # represents the first id
        expected_object_name = post.text
        self.assertEqual(expected_object_name, 'just a text')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text ='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')