import os
from datetime import datetime
from time import sleep
import json

from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base class init the base page that will be called from all pages"""
    EXTENDED = 120
    LONG = 30
    REGULAR = 5
    SHORT = 1

    def __init__(self, webdriver):
        self.driver = webdriver
        self.extended_wait = WebDriverWait(self.driver, self.EXTENDED)
        self.long_wait = WebDriverWait(self.driver, self.LONG)
        self.wait = WebDriverWait(self.driver, self.LONG)
        self.short_wait = WebDriverWait(self.driver, self.SHORT)
        self.action = ActionChains(self.driver)
        self.current_test = os.getenv('PYTEST_CURRENT_TEST').split(':')[0].replace('tests/', '').replace('.py', ''). \
            replace('/test', '_test')

    def __getattr__(self, loc):
        value = self.__dict__.get(loc.upper())
        if type(value) is tuple:
            locator = value
            try:
                self.get_presented_element(locator)
            except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                raise Exception(
                    f"An exception of type {type(e).__name__} occurred. "
                    f"Element with locator: {loc} = {locator} Class: {self.__class__.__name__}")
            element = self.get_presented_element(locator)
            element._locator = locator
            return element

    def init_all_elements(self):
        for key, value in self.__dict__.items():
            if type(value) is tuple:
                locator = value
                try:
                    self.get_presented_element(locator)
                except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                    raise Exception(
                        f"An exception of type {type(e).__name__} occurred. "
                        f"Element with locator: {key} = {locator} Class: {self.__class__.__name__}")

    def wait_request_and_get_response(self, request_uri: str, timeout: int = 10) -> dict:
        """
        Ожидаем завершение выполнения запроса, полученное тело ответа
        преобразуем словарь для дальнейшей обработки
        """
        request = self.driver.wait_for_request(request_uri, timeout)
        response_as_dict = json.loads(request.response.body)
        return response_as_dict

    def element_is_visible(self,
                           locator: tuple,
                           is_visible: bool = True
                           ) -> bool:
        """
        Проверка видимости/скрытости веб-элемента, используя стандартные условия
        для ожиданий. Параметр is_visible позволяет указать нам условие
        поверки элемента: is_visible=True - осуществляет проверку на видимость
        веб-элемента, is_visible=False - осуществляется проверка на скрытость веб-элемента.
        В случае, если ожидание возбуждает исключение TimeoutError, осуществляется его
        перехват, тем самым мы его глушим для возврата логического значения проверки
        """
        try:
            if is_visible:
                self.long_wait.until(EC.visibility_of_element_located(locator))
                return True
            else:
                self.long_wait.until(EC.invisibility_of_element_located(locator))
                return True
        except TimeoutError:
            return False

    def find_element_by_text(self, text):
        """
        :param text: Текст, по которому будет осуществлена попытка найти WebElement
        """
        locator = (By.XPATH, f'//*[contains(text(), "{text}")]')
        try:
            return self.get_presented_element(locator)
        except (TimeoutException, NoSuchElementException):
            return False

    def get_current_url(self):
        return self.driver.current_url

    def get_confirm_text(self):
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        return alert_text

    def get_text_from_element(self, locator):
        """Текст элемента"""
        element = self.get_presented_element(locator)
        return element.text

    def get_presented_element(self, *locators):
        try:
            return self.extended_wait.until(EC.presence_of_element_located(*locators))
        except TimeoutException:
            return False

    def wait_for_visibility(self, *locators):
        try:
            self.wait.until(EC.visibility_of_element_located(*locators))
        except TimeoutException:
            return False

    def wait_for_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_invisibility(self, *locators):
        self.extended_wait.until(EC.invisibility_of_element_located(*locators))

    def move_to_element(self, element):
        try:
            self.action.move_to_element(element).perform()
        except (TimeoutException, NoSuchElementException):
            return False

    def scroll_to_element(self, *locators):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView()", self.get_presented_element(*locators))
        except NoSuchElementException:
            return False

    def delay(self, sec):
        sleep(sec)

    def get_attr(self, attribute):
        return self.get_attribute(attribute)

    def go_to_iframe(self, iframe_name):
        return self.driver.switch_to.frame(iframe_name)

    def go_to_default_iframe(self):
        return self.driver.switch_to.default_content()


WebElement.get_attr = BasePage.get_attr
