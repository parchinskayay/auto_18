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


def test_by_id(driver):
    driver.get(URL)
    element = driver.find_element(By.ID, 'route-content')
    assert element.is_displayed()


def test_by_part_link(driver):
    driver.get(URL)
    element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Работать в Wildberries')
    assert element.is_displayed()


def test_by_link_text(driver):
    driver.get(URL)
    element = driver.find_element(By.LINK_TEXT, 'Работать в Wildberries')
    assert element.is_displayed()


def test_by_tag(driver):
    driver.get(URL)
    element = driver.find_element(By.TAG_NAME, 'header')
    assert element.is_displayed()


def test_by_class_name(driver):
    driver.get(URL)
    element = driver.find_element(By.CLASS_NAME, 'header__controls')
    assert element.is_displayed()
