from lesson22.pages.base_page import BasePage
from selenium.webdriver.common.by import By

BASE_URL = 'http://uitestingplayground.com/'


class UITestingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.VISIBILITY_TEXT = (By.XPATH, '//*[@class="container"]/p')
        self.CHECKBOX1 = (By.XPATH, '//*[@type="checkbox"][1]')
        self.CHECKBOX2 = (By.XPATH, '//*[@type="checkbox"][2]')
        self.SELECTOR = (By.ID, 'dropdown')
        self.SELECTOR_OPTION2 = (By.CSS_SELECTOR, '[value="2"]')
        self.DEMO = (By.XPATH, '//*[contains(text(), "Запустить демо")]')
        self.WINDOW = (By.CSS_SELECTOR, '[class="custom_btn btn_hover"]')
        self.IFRAME = (By.ID, 'iframe-1')
        self.IMG = (By.CSS_SELECTOR, '[src="img/logos/Browsers.png"]')
        self.FILE = (By.CSS_SELECTOR, '[type="file"]')

    def open_visibility(self):
        self.open_page(BASE_URL + 'visibility')

    def open_window(self):
        self.open_page('https://practice-automation.com/window-operations/')

    def open_irame(self):
        self.open_page('https://practice-automation.com/iframes/')

    def open_file(self):
        self.open_page('https://practice-automation.com/file-upload/')

    def open_checkboxes(self):
        self.open_page('https://the-internet.herokuapp.com/checkboxes')

    def open_dropdown(self):
        self.open_page('https://the-internet.herokuapp.com/dropdown')

    def open_learnjs(self):
        self.open_page('https://learn.javascript.ru/task/simple-page')

    def assert_that_visibility_has_text(self, text):
        self.assertions.assert_that_element_containce_text(self.VISIBILITY_TEXT, text)

    def assert_that_checkboxes_selected(self):
        self.assertions.assert_that_element_checked(self.CHECKBOX1, None)
        self.assertions.assert_that_element_checked(self.CHECKBOX2, 'true')

    def assert_that_checkboxes_selected2(self):
        self.assertions.assert_that_element_is_selected(self.CHECKBOX2)
        self.assertions.assert_that_element_is_not_selected(self.CHECKBOX1)

    def select_by_value_in_dropdown(self):
        self.select_by_visible_text(self.SELECTOR, 'Option 2')

    def assert_that_dropdown_selected(self):
        self.assertions.assert_that_attribute_is_visible(self.SELECTOR_OPTION2, 'selected', 'true')

    def open_demo(self):
        self.click(self.DEMO)

    def open_new_window(self):
        self.click(self.WINDOW)

    def assert_that_element_is_visible_button(self):
        self.assertions.assert_that_element_is_visible(self.WINDOW)

    def open_first_frame(self):
        self.switch_to_frame(self.IFRAME)

    def send_file_in_form(self):
        self.upload_file(self.FILE, '/Users/elenayanushevskaya/teachmeskills/auto_18/lesson22/pages/assert_elements_visible.png')