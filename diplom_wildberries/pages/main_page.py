from diplom_wildberries.elements import HeaderElement
from diplom_wildberries.helpers import BASE_URL
from diplom_wildberries.pages import BasePage
from selenium.webdriver.common.by import By


class MainLocators:
    HEADER = (By.CSS_SELECTOR, '[class="header"]')
    SLIDER = (By.XPATH, '//*[@class="slider"]')
    RECOMMENDATIONS = (By.CLASS_NAME, 'recommendations')


class MainPage(BasePage, MainLocators, HeaderElement):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def assert_that_main_is_opened(self):
        assert self.get_element(self.HEADER)
        assert self.get_element(self.SLIDER)
        assert self.get_element(self.RECOMMENDATIONS)
