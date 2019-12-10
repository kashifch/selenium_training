import time
import unittest
from selenium import webdriver

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Firefox()

    def test_login(self):
        # Open the target page
        self.driver.get('https://dummy-page')
        # Assert that 'edX' is present in browser title
        self.assertIn('edX', self.driver.title)
        # Find and fill the email field
        email_elem = self.driver.find_element_by_css_selector('deummy_elail')
        email_elem.send_keys('temp_user@yopmail.com')
        #Find and fill the password field
        pwd_elem = self.driver.find_element_by_css_selector('dummy_password')
        pwd_elem.send_keys('edxedxedx1')
        # Find and click the submit button
        subnit_elem = self.driver.find_element_by_css_selector('dummy_button')
        subnit_elem.click()
        #JUST FOR TRAINING PURPOSES< DON"T USE 'time.sleep' IN ACTUAL TESTS
        time.sleep(5)
        # Assert that 'Dashboard' is present in target pages browser title
        self.assertIn('Dashboard', self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

