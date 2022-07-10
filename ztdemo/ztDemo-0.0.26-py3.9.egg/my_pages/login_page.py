
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait

from base_page import BaseAPIPage, BasePage


class LoginPage(BasePage):
    input_email = (By.ID, "account")
    input_password = (By.ID, "password")
    button_login = (By.XPATH, '//*[@id="submit"]')
    user_status_after_login = (By.XPATH, '//*[@id="siteNav"]/a[2]')
    login_via_account = (By.XPATH, '//*[@id="loginCommon"]/ul/li[3]/a')
    we_chat_qr_code = (By.ID, 'qrcode')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.page_url = self.base_url + '/user-login.html'

    def login(self, user_name, password):
        self.open_page(self.page_url)
        self.driver.implicitly_wait(10)

        wait.WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'qrcode')))
        assert self.driver.find_element(*self.we_chat_qr_code).is_displayed()
        self.driver.find_element(*self.login_via_account).click()
        assert self.driver.find_element(*self.input_email).is_displayed()
        self.driver.find_element(*self.input_email).clear()
        self.driver.find_element(*self.input_email).send_keys(user_name)
        self.driver.find_element(*self.input_password).clear()
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.input_password).send_keys(Keys.RETURN)
        text = self.get_login_user_text()
        assert "退出" in text

    def get_login_user_text(self):
        if self.is_element_exists(self.user_status_after_login):
            return self.driver.find_element(*self.user_status_after_login).text
        return None


class LoginAPI(BaseAPIPage):

    def __init__(self, url):
        super().__init__(url)
        self.page_url = self.base_url + '/user-login.html'

    def login(self, user_name, password):
        data = {"account": user_name, "password": password}
        return self.post_api(self.page_url, headers=self.header_form, data=data)

    def get_login_cookie(self, user_name, password):
        self.login(user_name, password)
        # 获取Cookies
        return self.driver.cookies._cookies["www.zentao.net"]["/"]