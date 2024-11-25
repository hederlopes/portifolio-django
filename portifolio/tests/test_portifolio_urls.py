from django.test import TestCase
from django.urls import reverse


class PortfolioUrlTest(TestCase):
    def test_the_portifolio_home_is_correct(self):
        url = reverse('portifolio:home')
        self.assertEqual(url, '/')

    def test_the_portifolio_manager_is_correct(self):
        url = reverse('portifolio:manager')
        self.assertEqual(url, '/manager/')

    def test_the_portifolio_features_is_correct(self):
        url = reverse('portifolio:features')
        self.assertEqual(url, '/features/')

    def test_the_portifolio_contact_is_correct(self):
        url = reverse('portifolio:contact')
        self.assertEqual(url, '/contact/')

    def test_the_portifolio_about_is_correct(self):
        url = reverse('portifolio:about')
        self.assertEqual(url, '/about/')

    def test_the_portifolio_blog_is_correct(self):
        url = reverse('portifolio:blog')
        self.assertEqual(url, '/blog/')

    def test_the_portifolio_post_is_correct(self):
        url = reverse('portifolio:post', kwargs={'id': 1})
        self.assertEqual(url, '/post/1/')

    def test_the_portifolio_resume_is_correct(self):
        url = reverse('portifolio:resume')
        self.assertEqual(url, '/resume/')
