import time
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from helpers.api_client import LoginApi

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
        self.login_api = LoginApi()

    def test_login(self):
        # Open the target page
        self.login_api.authenticate(self.driver)
        self.dashboard.go_to_courses_page()
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

