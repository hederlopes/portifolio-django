from django.test import TestCase
from django.urls import reverse, resolve
from portifolio import views
from unittest import skip


class PortfolioViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('portifolio:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_manager_view_function_is_correct(self):
        view = resolve(reverse('portifolio:manager'))
        self.assertIs(view.func, views.manager)

    def test_recipe_features_view_function_is_correct(self):
        view = resolve(reverse('portifolio:features'))
        self.assertIs(view.func, views.features)

    def test_recipe_contact_view_function_is_correct(self):
        view = resolve(reverse('portifolio:contact'))
        self.assertIs(view.func, views.contact)

    def test_recipe_blog_view_function_is_correct(self):
        view = resolve(reverse('portifolio:blog'))
        self.assertIs(view.func, views.blog)

    def test_recipe_post_view_function_is_correct(self):
        view = resolve(reverse('portifolio:post', kwargs={'id': 1}))
        self.assertIs(view.func, views.post)

    def test_recipe_about_view_function_is_correct(self):
        view = resolve(reverse('portifolio:about'))
        self.assertIs(view.func, views.about)

    def test_recipe_resume_view_function_is_correct(self):
        view = resolve(reverse('portifolio:resume'))
        self.assertIs(view.func, views.resume)

    def test_portifolio_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:home'))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_manager_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:manager'))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_features_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:features'))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_contact_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:contact'))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_blog_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:blog'))
        self.assertEqual(response.status_code, 200)

    @skip('Verificar o object_404 na view')
    def test_portifolio_post_view_returns_status_code_200_ok(self):
        response = self.client.get(
            reverse('portifolio:post', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_about_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:about'))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_resume_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('portifolio:resume'))
        self.assertEqual(response.status_code, 200)

    def test_portifolio_home_view_loads_correct_template(self):
        template = self.client.get(reverse('portifolio:home'))
        self.assertTemplateUsed(template, 'portifolio/pages/home.html')

    def test_portifolio_blog_view_loads_correct_template(self):
        template = self.client.get(reverse('portifolio:blog'))
        self.assertTemplateUsed(template, 'portifolio/pages/blog.html')

    def test_portifolio_home_template_shows_no_recipes_found_if_no_recipes(self):  # noqa E501
        template = self.client.get(reverse('portifolio:home'))
        self.assertIn(
            'Welcome to my first project developed',
            template.content.decode('utf-8'),
        )
