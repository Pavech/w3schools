from selenium.webdriver.common.by import By

from ui_elements.base_page import BasePage


class TrySQLPage(BasePage):
    COMMAND_SQL_CUSTOMERS = (By.XPATH, "//*[contains(text(),'SELECT * FROM Customers;')]")
    TABLE_CUSTOMERS = (By.XPATH, "//td[@onclick='w3schoolsNoWebSQLSelectStar('Customers')']")
    CODE_SQL = (By.ID, "textareaCodeSQL")
    CONTACT_NAME = (By.XPATH, "//*[contains(text(),'{name}')]")
    ADDRESS = (By.XPATH, "//*[contains(text(),'{address}')]")
    NUM_RECORD = (By.XPATH, "//*[contains(text(),'Number of Records: {number}')]")

    """
        Команда для второго теста:
        **************************
        SELECT * FROM Customers
        WHERE City="London"
    """

    def choice_table_customers(self):
        self.click_element(locator=self.TABLE_CUSTOMERS)
        return self
