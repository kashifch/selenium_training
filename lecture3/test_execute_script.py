import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class EdxRegister(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome()
        # Open the target page
        self.driver.get('https://courses.stage.edx.org/register')

    def test_javascript(self):
        script = 'document.querySelector(".input-block.checkbox").click();'
        self.driver.execute_script(script)
        import time; time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

