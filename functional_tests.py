from selenium import webdriver
import unittest

#tests are arranged in classes which inherit from unittest.Testcase
class NewVisitorTest(unittest.TestCase):

    #starts before each test
    def setUp(self):
        #creates a selenium webbrowser object
        self.browser = webdriver.Firefox()
    #starts after each test
    def tearDown(self):
        #close browser object
        self.browser.quit()
    #them main function of our test so far
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        # open project homepage in selenium
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists
        # check to see if 'To-Do' is inside the browser's title attribute
        self.assertIn('To-Do', self.browser.title)
        #self.fail fails no matter what. this just returns a message
        self.fail('Finish the test!')
        # She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is trying fly-fishing lures)
        # When she hits enter, the page updates, and the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to makes a fly" (Edith is very methodical)
        # The page updates again, and not shows both items on her list
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her == there is some
        # explanatory text to that effect.
        # She visits that URL - her to-do list is still there.
        # Satisfied, she back to sleep
#onlu run if ran on its own
if __name__ == '__main__':
    #run our tests
    unittest.main(warnings='ignore')
