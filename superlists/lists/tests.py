#resolves URLs and finds out what view function they should be mapped to
from django.urls import resolve
#imports a special version of unittest's TestCase
from django.test import TestCase
#import the django HttpRequest
from django.http import HttpRequest

#imports the views.py function that we're gonna write later
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # check the root of the site and find the funciton
        found = resolve('/')
        # check if found.func (resolve.func) == what out home_page function
        # will return
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        #create an HttpRequest object
        request = HttpRequest()
        #call our home_page question with request as our arguement
        #store what it returns in 'response'
        response = home_page(request)
        #since the content of the response is raw bytes, we need to decode
        #into utf8
        #assign the decoded response to 'html'
        html = response.content.decode('utf8')
        #make sure that 'html' has an html tag up front
        self.assertTrue(html.startswith('<html>'))
        #make sure that it has a title called To-Do lists
        self.assertIn('<title>To-Do lists</title>', html)
        #make sure that it ends with </html>
        self.assertTrue(html.endswith('</html>'))
