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


def test_by_xpath_tag1(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//main')
    assert element.is_displayed()


def test_by_xpath_all(driver):
    driver.get(URL)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, '//*')
    assert element.is_displayed()


def test_by_xpath_id(driver):
    driver.get(URL)
    element = driver.find_element(By.XPATH, '//*[@id="route-content"]')
    assert element.is_displayed()


def test_by_xpath_class_and_list(driver):
    driver.get(URL)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, '(//*[@class="product-snippet"])[56]')
    assert element.is_displayed()


def test_by_xpath_contains_text(driver):
    driver.get(URL)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, "(//*[contains(text(), 'Корзина')])")
    assert element.is_displayed()


def test_by_xpath_contains_class(driver):
    driver.get(URL)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, "(//*[contains(@class, 'search')])")
    assert element.is_displayed()


def test_by_xpath_text(driver):
    driver.get(URL)
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR, '(//*[text()="Корзина"])')
    assert element.is_displayed()
