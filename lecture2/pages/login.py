from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True

    def fill_form(self):
        email_elem = self.driver.find_element_by_css_selector('#login-email')
        email_elem.send_keys('.....')
        #Find and fill the password field
        pwd_elem = self.driver.find_element_by_css_selector('#login-password')
        pwd_elem.send_keys('.....')

    def submit_form(self):
        subnit_elem = self.driver.find_element_by_css_selector('button[type="submit"]')
        subnit_elem.click()


