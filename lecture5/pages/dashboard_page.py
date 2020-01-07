from .base_page import BasePage
from .courses_page import CoursesPage

class DashboardPage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('.btn-neutral').is_displayed()

    def go_to_courses_page(self):
        self.find_elem('.btn-neutral').click()
        CoursesPage(self.driver).wait_for_page()
