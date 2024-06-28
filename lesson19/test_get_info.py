import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
URL = 'https://www.reddit.com'

@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()

def test_get_info_about_page(driver_firefox):
    driver_firefox.get(URL)
    time.sleep(1)

    assert URL in driver_firefox.current_url
    assert driver_firefox.title == 'Reddit - Dive into anything'
    assert driver_firefox.page_source
