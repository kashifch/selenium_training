import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_login(self):
        # Open the target page
        self.driver.get('https://*****/login')
        self.login.fill_form('temp_user@yopmail.com', 'edxedxedx1')
        self.login.submit_form()
        self.dashboard.go_to_courses_page()
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

