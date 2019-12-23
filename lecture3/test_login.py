import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.dashboard = Dashboard(self.driver)

    def test_login(self):
        # Open the target page
        self.driver.get('https://courses.stage.edx.org/login')
        # Assert that 'edX' is present in browser title
        self.assertTrue(self.login.is_browser_on_the_page())
        # Find and fill the email field
        self.login.fill_form()
        # Find and click the submit button
        self.login.submit_form()
        # Assert that 'Dashboard' is present in target pages browser title
        self.dashboard.is_browser_on_the_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

