import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

class AlertTest(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:5500/test_stub.html')
        self.alert = Alert(self.driver)

    # def test_accept_alert(self):
    #     self.driver.find_element_by_css_selector('button').click()
    #     time.sleep(2)
    #     self.alert.accept()

    def test_reject_alert(self):
        self.driver.find_element_by_css_selector('button').click()
        time.sleep(2)
        self.alert.dismiss()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

