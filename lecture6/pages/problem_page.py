from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


class ProblemPage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('.drag-container').is_displayed()

    def attempt_drag_and_drop(self):
        source = self.find_elem('.option[data-value="0"]')
        target = self.find_elem('[id*="top"]')
        action = ActionChains(self.driver)
        self.driver.execute_script("window.scrollTo(0, 500)")
        action.drag_and_drop(source, target).perform()
        import time; time.sleep(5)
        self.find_elem('.reset-button').click()

    def switch_to_iframe(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        iframe = self.find_elem('#iframe_236659462a3e4c6cabad1554ebd81dcd_2_1')
        self.driver.switch_to.frame(iframe)
        dropdown = Select(self.find_elem('.choices'))
        dropdown.select_by_visible_text('correct')
        self.driver.switch_to.default_content()
        self.find_elem('.option[data-value="0"]')
        import time; time.sleep(5)
    
