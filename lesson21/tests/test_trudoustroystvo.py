from lesson21.pages import TrudoustroystvoPage
from lesson21.pages.demoqa_page import DemoQA


def test_open_page(driver):
    page = TrudoustroystvoPage(driver)
    page.open()

    page.assert_elements_visible()


def test_fill_form(driver):
    page = DemoQA(driver)
    page.open()

    page.fill_form()

    page.assertions.assert_that_attribute_is_visible('awsedfr', 'wserf')