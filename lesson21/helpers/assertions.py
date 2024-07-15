from selenium.webdriver.common.by import By


class Assertions:

    def __init__(self, driver):
        self.driver = driver

    def assert_that_text_is_visible(self, selector, text, by=By.XPATH):
        el = self.driver.find_element(by, selector)
        assert el.text == text

    def assert_that_element_is_visible(self, selector, by=By.XPATH):
        assert self.driver.find_element(by, selector)

    def assert_that_attribute_is_visible(self, selector, attribute, value, by=By.XPATH):
        el = self.driver.find_element(by, selector)
        assert el.get_attribute(attribute) == value

    def assert_that_attribute_class_is_visible(self, selector, value, by):
        self.assert_that_attribute_is_visible(selector, 'class', value, by)
