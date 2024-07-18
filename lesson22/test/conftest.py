import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest


def pytest_addoption(parser):
    parser.addoption("--brw",
                     action="store",
                     default="chrome",
                     help="the name of the browser")

    parser.addoption("--headless",
                     action="store",
                     default="true",
                     help="the name of the browser")


@pytest.fixture
def driver(request):
    value = request.config.getoption("--brw")
    headless = request.config.getoption("--headless")

    if value == 'chrome':
        if headless:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.implicitly_wait(5)
            driver.maximize_window()

            yield driver

            driver.close()
            driver.quit()
