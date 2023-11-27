from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time=20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_element(self, locator):
        return self.app.driver.find_element_by_xpath(locator)

    def click_element(self, locator):
        """
        Click element.
        """
        element = self._find_element(locator)
        element.click()

    def fill(self, locator, value: str, wait_time=20):
        """
        Fill element (fill == send_keys)
        :param data: string to fill
        """
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        """
        Get element text.
        """
        element = self._find_element(locator, wait_time)
        return element.text

    def open_page(self, url: str):
        """
        Open page.
        """
        self.app.driver.get(url)

    def clear(self, locator, wait_time=20):
        """
        Clear element.
        """
        element = self._find_element(locator, wait_time)
        element.clear()
