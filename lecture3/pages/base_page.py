from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class element_has_color(object):

    def __init__(self, locator, elem_color):
        self.locator = locator
        self.elem_color = elem_color
    
    def __call__(self, driver):
        elem_color = driver.find_element(*self.locator).value_of_css_property('background-color')
        if elem_color == self.elem_color:
            return elem_color
        else:
            return False

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_elem(self, css_selector):
        try: 
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} not found')

    def find_elems(self, css_selector):
        try: 
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} not found')

    def wait_for_element_visibility(self, css_selector, timeout=10):
        try: 
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} not found')

    def wait_for_element_to_be_clickable(self, css_selector, timeout=10):
        try: 
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            raise TimeoutException(f'{css_selector} not found')

    def wait_for_partial_title_match(self, title_text, timeout=10):
        try: 
            return WebDriverWait(self.driver, timeout).until(EC.title_contains(title_text))
        except TimeoutException:
            raise TimeoutException(f'{self.driver.title} does not contain {title_text}')

    def wait_for_exact_title_match(self, title_text, timeout=10):
        try: 
            return WebDriverWait(self.driver, timeout).until(EC.title_is(title_text))
        except TimeoutException:
            raise TimeoutException(f'{self.driver.title}: does not match {title_text}')

    def wait_for_element_text(self, css_selector, elem_text, timeout=10):
        try: 
            return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), elem_text))
        except TimeoutException:
            raise TimeoutException(f'{elem_text}: does not match {self.find_elem(css_selector).text}')

    def wait_for_element_color(self, css_selector, elem_color, timeout=10):
        try: 
            return WebDriverWait(self.driver, 10).until(element_has_color((By.CSS_SELECTOR, css_selector), elem_color))
        except TimeoutException:
            raise TimeoutException(f'Color does not match')