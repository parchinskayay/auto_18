import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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


def test_google():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.google.com/')
    element = driver.find_element(By.XPATH, '//textarea[@class="gLFyf"]')
    element.send_keys("selenium documentation webdriver")
    time.sleep(2)

    element = driver.find_element(By.CSS_SELECTOR, '[class="gNO89b"]')
    element.click()
    time.sleep(2)

    element_links = driver.find_elements(By.XPATH, '//*[@href="https://www.selenium.dev/documentation/webdriver/"]')

    assert len(element_links) == 2

    element_links[0].click()
    assert driver.current_url == 'https://www.selenium.dev/documentation/webdriver/'

    driver.close()
    driver.quit()