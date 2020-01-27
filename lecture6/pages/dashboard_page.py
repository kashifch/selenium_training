from .base_page import BasePage
from .courses_page import CoursesPage
from .course_page import CoursePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class DashboardPage(BasePage):

    def is_browser_on_page(self):
        return self.find_elem('.btn-neutral').is_displayed()

    def go_to_courses_page(self):
        self.find_elem('.btn-neutral').click()
        CoursesPage(self.driver).wait_for_page()

    def go_to_target_course(self, course_id):
        self.find_elem(f'.course-title [data-course-key="{course_id}"]').click()
        CoursePage(self.driver).wait_for_page()

    def open_course_in_new_tab(self, course_id):
        actions = ActionChains(self.driver)
        course = self.find_elem(f'.course-title [data-course-key="{course_id}"]')
        actions.key_down(Keys.COMMAND).click(course).key_up(Keys.COMMAND).perform() 
        self.driver.switch_to.window(self.driver.window_handles[1])
        import time; time.sleep(10)
        CoursePage(self.driver).wait_for_page()

    def open_course_in_new_window(self, course_id):
        course = self.find_elem(f'.course-title [data-course-key="{course_id}"]')
        course_link = course.get_attribute('href')
        self.driver.execute_script("window.open(arguments[0], height=100, width=100);", course_link)
        self.driver.switch_to.window(self.driver.window_handles[1])
        import time; time.sleep(10)
        CoursePage(self.driver).wait_for_page()
