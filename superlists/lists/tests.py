#resolves URLs and finds out what view function they should be mapped to
from django.urls import resolve
#imports a special version of unittest's TestCase
from django.test import TestCase
#imports the views.py function that we're gonna write later
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # check the root of the site and find the funciton
        found = resolve('/')
        # check if found.func (resolve.func) == what out home_page function
        # will return
        self.assertEqual(found.func, home_page)
