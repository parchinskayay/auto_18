from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, selector):
        element = self.driver.find_element(By.XPATH, selector)
        element.click()

    def fill(self, selector, text):
        element = self.driver.find_element(By.XPATH, selector)
        element.send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)
