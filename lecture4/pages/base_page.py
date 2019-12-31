from abc import abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class element_has_color(object):
    """An expectation for checking that an element has a particular background color.

    locator - used to find the element
    returns the WebElement once it has the particular background color
    """
    def __init__(self, locator, background_color):
        self.locator = locator
        self.background_color = background_color

    def __call__(self, driver):
        element_color = driver.find_element(*self.locator).value_of_css_property('background-color')
        if element_color == self.background_color:
            return element_color
        else:
            return False

class is_document_ready(object):
    """An expectation for checking that an element has a particular background color.

    locator - used to find the element
    returns the WebElement once it has the particular background color
    """
    def __call__(self, driver):
        page_status = driver.execute_script("return document.readyState=='complete'")
        # import pdb; pdb.set_trace()
        return page_status


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def is_browser_on_page(self):
        return False

    def find_elem(self, css_selector, timeout=20):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} not found')

    def wait_for_element_visibility(self, css_selector, timeout=30):
        try:
            return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} is not visible')

    def wait_for_partial_title_match(self, title_string, timeout=30):
        try:
            return WebDriverWait(self.driver, 30).until(EC.title_contains(title_string))
        except TimeoutException:
            raise TimeoutException(f'{title_string} is not present in {self.driver.title}')

    def wait_for_element_text(self, css_selector, target_string, timeout=30):
        try:
            return WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), target_string))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} is not visible')

    def wait_for_element_color(self, css_selector, target_color, timeout=30):
        try:
            return WebDriverWait(self.driver, 30).until(element_has_color((By.CSS_SELECTOR, css_selector), target_color))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} does not have the {target_color} color')

    def wait_for_page(self, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(is_document_ready())
        except TimeoutException:
            raise TimeoutException(f'Page is not loaded completely: {self}')

        try:
            return WebDriverWait(self.driver, timeout).until(lambda x: (self.is_browser_on_page(), self))
        except TimeoutException:
            raise TimeoutException(f'Page is not on correct page: {self}')

      