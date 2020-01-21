import time
import os
import unittest
import csv
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

class EdxLogin(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_login_using_csv(self):
        self.driver.get('https://courses.edx.org/login')
        filename = 'credentials.csv'
        user_file = os.path.abspath(os.path.join(os.curdir, filename))
        with open(user_file) as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                self.login.fill_form(row[0], row[1])
                self.login.submit_form()
        self.dashboard.go_to_courses_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

