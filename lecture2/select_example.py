import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class EdxRegister(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()

    def test_register(self):
        # Open the target page
        self.driver.get('https://......../register')
        country_elem = Select(self.driver.find_element_by_css_selector('#register-country'))
        country_elem.select_by_visible_text('Pakistan')
        import time; time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

