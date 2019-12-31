from .base_page import BasePage

class CoursesPage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('.js-featured-results').is_displayed()
