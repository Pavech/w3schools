import logging
import pytest
from selenium import webdriver as web_wire
from selenium.webdriver import DesiredCapabilities

from model.app import Application

logger = logging.getLogger("w3schools")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default='test',
                     help="defines current environment (test or stage)")
    parser.addoption("--headless", action="store", default='false',
                     help="headless mode")


@pytest.fixture(scope='session')
def cmdopt(request):
    args = {
        'env': request.config.getoption("--env"),
        'headless': request.config.getoption("--headless")}
    return args


# @pytest.fixture
# def ui_driver(request):
#     url = request.config.getoption("--url")
#     logger.info(f"Start app on {url}")
#     headless = request.config.getoption("--headless")
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("window-size=1800,1080")
#     if headless:
#         chrome_options.headless = True
#     else:
#         chrome_options.headless = False
#     driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe", options=chrome_options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
@pytest.fixture
def app(web_start_page):
    app = Application(webdriver=web_start_page)
    yield app


@pytest.fixture()
def webdriver(cmdopt):
    desired_capabilities = DesiredCapabilities.CHROME.copy()  # chrome driver should be in PATH env
    desired_capabilities["unexpectedAlertBehaviour"] = "ignore"
    desired_capabilities["acceptSslCerts"] = True

    options = web_wire.ChromeOptions()

    options.add_argument('--window-size=1920,1080')
    options.add_argument('--force-device-scale-factor=0.90')
    if cmdopt['headless'] == 'true':
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        options.add_argument('--no-sandbox')
    options.add_argument('--ignore-ssl-errors')

    if cmdopt['headless'] == 'false':
        driver = web_wire.Chrome(desired_capabilities=desired_capabilities, options=options)
    else:
        raise ValueError("Неверное значение для аргумента --driver-setting. Возможны local и host")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def web_start_page(webdriver):
    webdriver.get("https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all")
    return webdriver
