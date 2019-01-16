#import the selenium browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#looks like we're gonna write a time dependant test
import time
#import pythons unittest
import unittest

#tests are arranged in classes which inherit from unittest.Testcase
#this test imitates the 'new user' experience
class NewVisitorTest(unittest.TestCase):

    #starts before each test
    def setUp(self):
        #creates a selenium webbrowser object
        self.browser = webdriver.Firefox()

    #starts after each test
    def tearDown(self):
        #close browser object
        self.browser.quit()

    #we ran somthing similar to this 3 times in a row.
    #whenever we run something 3 times in 1 script, refactor it into a funciton
    def check_for_row_in_list_table(self, row_text):
        #assign the element with id 'id_list_table'
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    #them main function of our test so far
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        # open project homepage in selenium
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        # check to see if 'To-Do' is inside the browser's title attribute
        self.assertIn('To-Do', self.browser.title)
        #use selenium to assign the text in <h1> header to 'header_text'
        header_text = self.browser.find_element_by_tag_name('h1').text
        #check to make sure 'To-Do' is in header_text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        #use selenium to locate an element with the id 'id_new_item
        #assign this element to the variable inputbox
        inputbox = self.browser.find_element_by_id('id_new_item')
        #get an attibute from that element named 'placeholder'
        #and see if it's equal to 'Enter a to-do item'
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is trying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to makes a fly" (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and not shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her == there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.
        
        # Satisfied, she back to sleep

#onlu run if ran on its own
if __name__ == '__main__':
    #run our tests
    unittest.main(warnings='ignore')

#self.fail fails no matter what. this just returns a message
#self.fail('Finish the test!')
