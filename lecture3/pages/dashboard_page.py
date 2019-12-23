from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage

class Dashboard(BasePage):

    # def is_browser_on_the_page(self):
    #     self.wait_for_element_visibility('.btn-neutral')
    #     return True

    # def is_browser_on_the_page(self):
    #     self.wait_for_exact_title_match('Dashboard')
    #     return True

    def is_browser_on_the_page(self):
        self.wait_for_element_text('.btn-neutral', 'Explore New Courses')
        return True