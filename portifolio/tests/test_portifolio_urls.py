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
    
    def test_the_portifolio_resume_is_correct(self):
        url = reverse('portifolio:resume')
        self.assertEqual(url, '/resume/')
    
    def test_portifolio_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:home'))
        self.assertEqual(response.status_code,200)

    def test_portifolio_home_view_loads_correct_template(self):
        template = self.client.get(reverse('portifolio:home'))
        self.assertTemplateUsed(template, 'portifolio/pages/home.html')

    def test_portifolio_home_template_shows_no_recipes_found_if_no_recipes(self):
        template = self.client.get(reverse('portifolio:home'))
        self.assertIn(
            'Welcome to my first project developed',
            template.content.decode('utf-8'),
            )
