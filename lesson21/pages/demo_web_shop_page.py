from lesson21.locators import DemoWebShopLocators
from lesson21.pages import BasePage
from selenium.webdriver.common.by import By


class DemoWebShopPage(BasePage, DemoWebShopLocators):

    def __init__(self, driver):
        super().__init__(driver)


    def open(self):
        self.driver.get('https://demowebshop.tricentis.com/')
        return self

    def assert_elements_visible(self):
        self.assert_that_element_is_visible(self.EMAIL_INPUT)
        self.assert_that_element_is_visible(self.SUBSCRIBE_BUTTON)

        self.save_screenshot('assert_elements_visible.png')
        return self
