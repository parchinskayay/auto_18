import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

URL = 'https://www.wildberries.by/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()

def test_by_css_class_name1(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '.slider__item.is-active')
    assert element.is_displayed()


def test_by_css_class_name2(driver):
    driver.get(URL)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, '.skeleton-animation')
    assert element.is_displayed()


def test_by_css_id(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '#wbx-notification')
    assert element.is_displayed()


def test_by_css_tags(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'div')
    assert element.is_displayed()


def test_by_css_tags_atrr1(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, "a[data-text='strBecomeASeller']")
    assert element.is_displayed()


def test_by_css_tags_atrr2(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, "[data-text='strBecomeASeller']")
    assert element.is_displayed()


def test_by_css_tags_atrr3(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, "[data-tag='becomeASeller']")
    assert element.is_displayed()


def test_by_css_tags_atrr4(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, "[class='header__links']")
    assert element.is_displayed()


def test_by_css_tags_atrr5(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '[class="header__top header__container"]')
    assert element.is_displayed()


def test_by_css_tags_start_of_the_str(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'a[href^="https"]')
    assert element.is_displayed()


def test_by_css_tags_sub_str(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, 'a[href*="https"]')
    assert element.is_displayed()

def test_by_css_parents(driver):
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '[class="header"] [class="header__wrapper"]')
    assert element.is_displayed()
