from lesson21.base_page import BasePage
from selenium.webdriver.common.by import By

from lesson21.urls import BASE_PATH


class TrudoustroystvoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.EMPLOYMENT_INTRO = '.employment__intro'
        self.STORAGE_TAG = '[data-target="#storage"]'

    def open(self):
        self.driver.get(BASE_PATH + 'services/trudoustroystvo')

    def assert_elements_visible(self):
        assert self.driver.find_element(By.CSS_SELECTOR, self.EMPLOYMENT_INTRO)
        assert self.driver.find_element(By.CSS_SELECTOR, self.STORAGE_TAG)

        self.save_screenshot('assert_elements_visible.png')
