import requests
from requests.exceptions import HTTPError

class UserSessionApiBase(object):

    def __init__(self):
        self.session = requests.Session()
        self.base_url = ''
        self.post_url = ''
        self.referer_url = ''
        self.target_page_url = ''
        
    def post_headers(self, x_csrf):
        return {
            'Referer': self.referer_url,
            'X-CSRFToken': x_csrf
        }

    def open_base_page(self):
        try:
            response = self.session.get(self.base_url)
            response.raise_for_status()
            self.session.headers = self.post_headers(self.session.cookies['csrftoken'])
        except HTTPError as http_err:
            print (f'Response failed with error: {http_err}')

    def create_user_session(self):
        post_data = {
            'email': 'temp_user@yopmail.com',
            'password': 'edxedxedx1'
        }
        try:
            response = self.session.post(self.post_url, data=post_data)
            response.raise_for_status()
        except HTTPError as http_err:
            print (f'Response failed with error: {http_err}')

    def authenticate(self, driver):
        self.open_base_page()
        self.create_user_session()
        driver.get(self.target_page_url)
        for cookie in self.session.cookies:
            driver.delete_cookie(cookie.name)
            driver.add_cookie({
                "name": cookie.name,
                "value": cookie.value,
                "path": cookie.path,
                "expiry": cookie.expires
            })
        driver.get(self.target_page_url)


class LoginApi(UserSessionApiBase):

    def __init__(self):
        super(LoginApi, self).__init__()
        self.base_url = 'https://courses.stage.edx.org/login'
        self.post_url = 'https://courses.stage.edx.org/user_api/v1/account/login_session/'
        self.referer_url = 'https://courses.stage.edx.org/login'
        self.target_page_url = 'https://courses.stage.edx.org/dashboard'


