import time
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.course_page import CoursePage
from helpers.api_client import LoginApi

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.login_api = LoginApi('temp_user@yopmail.com', 'edxedxedx1')

    def test_switch_window(self):
        self.login_api.authenticate(self.driver)
        current_window = self.driver.current_window_handle
        self.dashboard.open_course_in_new_window('course-v1:edx+TEST01+2019')
        self.driver.switch_to.window(current_window)
              
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

