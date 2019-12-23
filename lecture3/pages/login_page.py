from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .base_page import BasePage

class LoginPage(BasePage):

    def is_browser_on_the_page(self):
        self.wait_for_element_visibility('button[type="submit"]')
        return True

    def fill_form(self):
        email_elem = self.find_elem('#login-email')
        email_elem.send_keys('temp_user@yopmail.com')
        #Find and fill the password field
        pwd_elem = self.find_elem('#login-password')
        pwd_elem.send_keys('edxedxedx1')

    def submit_form(self):
        # btn_elem = self.wait_for_element_to_be_clickable('.login-button')
        btn_elem = self.find_elem('.login-button')
        self.wait_for_element_color('.login-button', 'rgba(18, 111, 154, 1)')
        btn_elem.click()
