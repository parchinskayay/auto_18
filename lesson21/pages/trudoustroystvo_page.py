from lesson21.pages import BasePage
from selenium.webdriver.common.by import By

from lesson21.helpers import BASE_PATH


class TrudoustroystvoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.EMPLOYMENT_INTRO = '.employment__intro'
        self.STORAGE_TAG = '[data-target="#storage"]'

    def open(self):
        self.driver.get(BASE_PATH + 'services/trudoustroystvo')

    def assert_elements_visible(self):
        self.assertions.assert_that_element_is_visible(self.EMPLOYMENT_INTRO)
        self.assertions.assert_that_element_is_visible(self.STORAGE_TAG)

        self.save_screenshot('assert_elements_visible.png')
