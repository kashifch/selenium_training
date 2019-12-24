from .base_page import BasePage

class LoginPage(BasePage):

    def is_browser_on_the_page(self):
        self.wait_for_element_visibility('button[type="submit"]')
        return True

    def fill_form(self):
        email_elem = self.find_elem('#login-email')
        email_elem.send_keys('.....@yopmail.com')
        #Find and fill the password field
        pwd_elem = self.find_elem('#login-password')
        pwd_elem.send_keys('.....')

    def submit_form(self):
        subnit_elem = self.find_elem('button[type="submit"]')
        # Wait for submit button to have blus color
        self.wait_for_element_color('.login-button', 'rgba(18, 111, 154, 1)')
        subnit_elem.click()


