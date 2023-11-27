import logging
import pytest
from selenium import webdriver

from model.app import Application

logger = logging.getLogger("w3schools")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all",
        help="w3schools",
    ),
    parser.addoption("--headless", action="store_true", help="Headless mode"),


@pytest.fixture
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start app on {url}")
    headless = request.config.getoption("--headless")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("window-size=1800,1080")
    if headless:
        chrome_options.headless = True
    else:
        chrome_options.headless = False
    driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe", options=chrome_options)
    app = Application(driver, url)
    yield app
    app.quit()
