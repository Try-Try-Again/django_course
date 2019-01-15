#resolves URLs and finds out what view function they should be mapped to
from django.urls import resolve
#imports a special version of unittest's TestCase
from django.test import TestCase
#import the django HttpRequest
from django.http import HttpRequest
from django.template.loader import render_to_string

#imports the views.py function that we're gonna write later
from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
