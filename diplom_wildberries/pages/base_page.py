from selenium.webdriver.common.by import By

from diplom_wildberries.helpers.assertions import Assertions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.assertions = Assertions(driver)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, selector):
        element = self.driver.find_element(selector)
        element.click()

    def fill(self, selector, text):
        element = self.driver.find_element(selector)
        element.send_keys(text)

    def get_element(self, selector):
        return self.driver.find_element(*selector)
    def add_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def get_text(self, selector):
        element = self.driver.find_element(*selector)
        return element.text