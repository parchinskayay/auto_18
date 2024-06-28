import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

URL = 'https://www.audi.com/en.html'


@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()


def test_audi(driver_firefox):
    driver_firefox.get(URL)

    assert driver_firefox.find_element(By.XPATH, '//*[@id="ensModalWrapper"]/div')



