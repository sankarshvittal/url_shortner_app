from django.test import TestCase
from .views import home_view
from django.urls import resolve


class HomePageTests(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_view)




