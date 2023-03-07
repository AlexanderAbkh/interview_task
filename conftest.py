import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pom.index_page import IndexPage



@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def setup(get_webdriver):
    driver = get_webdriver
    url = 'https://demoqa.com/'
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def index_page(setup):
    yield IndexPage(setup)
