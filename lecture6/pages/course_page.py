from .base_page import BasePage
from .problem_page import ProblemPage
from selenium.webdriver.common.action_chains import ActionChains
import time

class CoursePage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('[data-action-type="resume"]').is_displayed()

    def go_to_problem_page(self):
        self.find_elem('a.outline-item.focusable').click()
        ProblemPage(self.driver).wait_for_page()

    

    
