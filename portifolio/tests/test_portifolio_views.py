from django.test import TestCase
from django.urls import reverse, resolve
from portifolio import views

class PortfolioViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('portifolio:home'))
        self.assertIs(view.func,views.home)

    def test_recipe_manager_view_function_is_correct(self):
        view = resolve(reverse('portifolio:manager'))
        self.assertIs(view.func,views.manager)

    def test_recipe_features_view_function_is_correct(self):
        view = resolve(reverse('portifolio:features'))
        self.assertIs(view.func,views.features)

    def test_recipe_contact_view_function_is_correct(self):
        view = resolve(reverse('portifolio:contact'))
        self.assertIs(view.func,views.contact)

    def test_recipe_about_view_function_is_correct(self):
        view = resolve(reverse('portifolio:about'))
        self.assertIs(view.func,views.about)
    
    def test_recipe_resume_view_function_is_correct(self):
        view = resolve(reverse('portifolio:resume'))
        self.assertIs(view.func,views.resume)