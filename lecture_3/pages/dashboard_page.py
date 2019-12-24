from .base_page import BasePage

class DashboardPage(BasePage):

    # def is_browser_on_the_page(self):
    #     self.wait_for_partial_title_match('Dashboard')
    #     return True

    def is_browser_on_the_page(self):
        self.wait_for_element_text('.btn-neutral', 'Explore New Courses')
        return True
