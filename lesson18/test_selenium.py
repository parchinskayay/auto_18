import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
URL = 'https://www.selenium.dev/'

def test_selenium_assert():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(URL)
    element = driver.find_element(By.CSS_SELECTOR, '.selenium-button.selenium-webdriver')
    element.click()

    time.sleep(2)

    assert driver.current_url == 'https://www.selenium.dev/documentation/webdriver/'

    driver.close()
    driver.quit()