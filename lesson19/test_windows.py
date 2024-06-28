import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from lesson19.helpers import add_cookie

URL_1 = 'https://www.reddit.com'
URL_2 = 'https://www.youtube.com'


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver

    driver.close()
    driver.quit()


def test_window_handles(driver):
    driver.get(URL_1)

    driver.execute_script("window.open()")
    time.sleep(3)
    assert len(driver.window_handles) == 2


def test_switch(driver):
    driver.get(URL_1)

    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(URL_2)
    time.sleep(3)

    driver.save_screenshot('test_1.png')

    driver.switch_to.window(driver.window_handles[0])
    driver.save_screenshot('test_2.png')
