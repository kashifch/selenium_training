import time
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.course_page import CoursePage
from pages.problem_page import ProblemPage
from helpers.api_client import LoginApi

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.problem_page = ProblemPage(self.driver)
        self.login_api = LoginApi('temp_user@yopmail.com', 'edxedxedx1')

    def test_iframe(self):
        self.login_api.authenticate(self.driver)
        self.dashboard.go_to_target_course('course-v1:edx+TEST01+2019')
        self.course_page.go_to_problem_page()
        self.problem_page.switch_to_iframe()
        
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

