from selenium.webdriver.common.by import By

from lesson21.helpers import Assertions


class BasePage(Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.assertions = Assertions(driver)

    def click(self, selector, by=By.XPATH):
        element = self.driver.find_element(by, selector)
        element.click()

    def fill(self, selector, text, by=By.XPATH):
        element = self.driver.find_element(by, selector)
        element.send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)
