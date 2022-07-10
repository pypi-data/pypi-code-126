from selenium.webdriver.common.by import By

from ztDemo.my_pages.base_page import BasePage


class ScorePage(BasePage):

    score_status = (By.XPATH, '//div[@class="panel-heading"]/strong')

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.page_url = self.base_url + '/user-score.html'

    def get_score_text(self):
        if self.is_element_exists(self.score_status):
            return self.driver.find_element(*self.score_status).get_attribute("innerHTML")
        return None


