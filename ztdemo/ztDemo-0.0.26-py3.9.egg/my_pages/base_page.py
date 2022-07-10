import time

import requests
from selenium import webdriver


def cookie_to_selenium_format(cookie):
    cookie_selenium_mapping = {'path': '', 'secure': '', 'name': '', 'value': '', 'expires': ''}
    cookie_dict = {}
    if getattr(cookie, 'domain_initial_dot'):
        cookie_dict['domain'] = '.' + getattr(cookie, 'domain')
    else:
        cookie_dict['domain'] = getattr(cookie, 'domain')
    for k in list(cookie_selenium_mapping.keys()):
        key = k
        value = getattr(cookie, k)
        cookie_dict[key] = value
    return cookie_dict


class BasePage:
    def __init__(self, driver, base_url=None):
        if str(driver).capitalize() == "Chrome":
            self.driver = webdriver.Chrome()
        elif str(driver).capitalize() == "Firefox":
            self.driver = webdriver.Firefox()
        elif str(driver).capitalize() == "Safari":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome()
        self.base_url = base_url

    def open_page(self, url):
        self.driver.get(url)

    def is_element_exists(self, ele):
        time_out = 60
        flag = False
        while time_out > 0:
            try:
                self.driver.find_element(*ele)
                flag = True
                break
            except:
                time_out -= 1
                time.sleep(0.5)
        return flag

    def close_page(self):
        self.driver.quit()

    def open_page(self, url):
        self.driver.get(url)

    def is_element_exists(self, ele):
        time_out = 60
        flag = False
        while time_out > 0:
            try:
                self.driver.find_element(*ele)
                flag = True
                break
            except:
                time_out -= 1
                time.sleep(0.5)
        return flag

    def page_go(self, cookies):
        self.driver.get(self.page_url)
        time.sleep(1)

        # 删除所有cookies
        self.driver.delete_all_cookies()

        # 针对获取到API登录的cookie，写入WebDriver里
        for k, v in cookies.items():
            self.driver.add_cookie(cookie_to_selenium_format(v))
        time.sleep(1)
        # 此时， 拿到了登录态
        self.driver.get(self.page_url)


class BaseAPIPage:
    header_form = {'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8'}
    header_json = {'Content-Type': 'application/json', 'charset': 'UTF-8'}

    def __init__(self, url=None):
        self.driver = requests.session()
        self.base_url = url

    def post_api(self, url, headers=header_json, **kwargs):
        return self.driver.post(url, headers=headers, **kwargs)

    def get_api(self, url, headers=header_json, **kwargs):
        return self.driver.get(url, headers=headers, **kwargs)

    def put_api(self):
        pass
