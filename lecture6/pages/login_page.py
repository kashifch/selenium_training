from .base_page import BasePage
from .dashboard_page import DashboardPage

class LoginPage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('button[type="submit"]').is_displayed()

    def fill_form(self, user_email, user_password):
        email_elem = self.find_elem('#login-email')
        email_elem.clear()
        email_elem.send_keys(user_email)
        #Find and fill the password field
        pwd_elem = self.find_elem('#login-password')
        pwd_elem.clear()
        pwd_elem.send_keys(user_password)

    def submit_form(self):
        submit_elem = self.find_elem('button[type="submit"]')
        # Wait for submit button to have blue color
        self.wait_for_element_color('.login-button', 'rgba(18, 111, 154, 1)')
        submit_elem.click()
        # self.driver.execute_script("document.querySelector('.login-button').click()")
        DashboardPage(self.driver).wait_for_page()


