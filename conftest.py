import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or fr")


@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(executable_path='C:\Selenium Chrome\chromedriver.exe',
                               options=options)

    yield browser
    print("\nclosing the browser")
    browser.quit()


