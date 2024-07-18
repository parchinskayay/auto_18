import time

import pytest

from lesson22.pages.uitesting_page import UITestingPage


def test_get_text(driver):
    page = UITestingPage(driver)

    page.open_visibility()

    page.assert_that_visibility_has_text("Checking if element is visible on screen may be a non trivial task.")


def test_checkboxes(driver):
    page = UITestingPage(driver)

    page.open_checkboxes()

    page.assert_that_checkboxes_selected()


def test_checkboxes2(driver):
    page = UITestingPage(driver)

    page.open_checkboxes()

    page.assert_that_checkboxes_selected2()


def test_select__by_value(driver):
    page = UITestingPage(driver)

    page.open_dropdown()

    page.select_by_value_in_dropdown()
    time.sleep(3)
    page.assert_that_dropdown_selected()


def test_alert(driver):
    name = 'Elena'
    page = UITestingPage(driver)

    page.open_learnjs()
    page.open_demo()

    page.prompt(name)
    text = page.alert_accept()
    assert text == name


def test_window(driver):
    page = UITestingPage(driver)

    page.open_window()
    page.open_new_window()
    time.sleep(10)
    page.assert_that_element_is_visible_button()


@pytest.mark.only
def test_file(driver):
    page = UITestingPage(driver)

    page.open_file()
    page.send_file_in_form()
    time.sleep(10)
