from lesson21.locators import DemoWebShopLocators
from lesson21.pages import BasePage
from selenium.webdriver.common.by import By


class DemoQA(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

        self.NAME = '[id="firstName"]'
        self.MALE = '[class="custom-control custom-radio custom-control-inline"]'
        self.SPORT = '[class="custom-control custom-checkbox custom-control-inline"]'
        self.FILE = '[type="file"]'
        self.SUBMIT = '[type="submit"]'
        self.CITY = '[class="col-md-4 col-sm-12"]'
        self.LAST_NAME = '[id="lastName"]'
        self.USER_NUMBER = '[id="userNumber"]'


    def open(self):
        self.driver.get('https://demoqa.com/automation-practice-form')
        return self

    def fill_form(self):
        self.fill(self.NAME, By.CSS_SELECTOR, 'qwertg')
        self.fill(self.LAST_NAME, By.CSS_SELECTOR, 'qwertg')
        self.fill(self.USER_NUMBER, By.CSS_SELECTOR, '1234564545')
        self.click(self.MALE)
        self.fill(self.FILE, By.CSS_SELECTOR, '/Users/elenayanushevskaya/teachmeskills/auto_18/lesson19/test_2.png')
        self.click(self.SUBMIT)
