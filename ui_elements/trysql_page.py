# from selenium.webdriver.common.by import By
#
# from ui_elements.main_page import MainPage
#
#
# class TrySQLPage(MainPage):
#     def __init__(self, webdriver):
#         super().__init__(webdriver)
#         self.COMMAND_SQL_CUSTOMERS = (By.XPATH, "//*[contains(text(),'SELECT * FROM Customers;')]")
#         self.TABLE_CUSTOMERS = (By.XPATH, "//td[@onclick=\"w3schoolsNoWebSQLSelectStar('Customers')\"]")
#         self.CODE_SQL = (By.ID, "textareaCodeSQL")
#         self.CONTACT_NAME = (By.XPATH, "//*[contains(text(),'{name}')]")
#         self.TEST = (By.XPATH, "//*[contains(text(),'Поиск в Google')]")
#         self.ADDRESS = (By.XPATH, "//*[contains(text(),'{address}')]")
#         self.RUN_SQL = (By.XPATH, "//*[contains(text(),'Run SQL »')]/.")
#         self.NUM_RECORD = (By.XPATH, "//*[contains(text(),'Number of Records: {number}')]")
#
#     """
#         Команда для второго теста:
#         **************************
#         SELECT * FROM Customers
#         WHERE City="London"
#     """

#
#     def choice_table_customers(self):
#         # self.click_element(locator=self.BTN_RUN_SQL)
#         self.click(locator=self.TEST)
#
#     def click_test(self):
#         """Кликнуть открыть копилку"""
#         self.wait_for_visibility(self.RUN_SQL)
#         self.click(self.RUN_SQL)
#
#     # def choice_click_account(self):
#     #
#     #     self.wait_for_visibility(self.BTN_RUN_SQL)
#     #     self.click(self.BTN_RUN_SQL)
#     #     return self

"""
команда для третьего теста
INSERT INTO Customers (CustomersID)
VALUES (100)
"""
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from ui_elements.main_page import MainPage


class TrySQLPage(MainPage):

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.COMMAND_SQL_CUSTOMERS = (By.XPATH, "//*[contains(text(),'SELECT * FROM Customers;')]")
        self.TABLE_CUSTOMERS = (By.XPATH, "//td[@onclick=\"w3schoolsNoWebSQLSelectStar('Customers')\"]")
        self.CODE_SQL = (By.ID, "textareaCodeSQL")
        self.RUN_SQL = (By.XPATH, "//*[contains(text(),'Run SQL »')]/.")
        self.NUM_RECORD = (By.XPATH, "//*[contains(text(),'Number of Records: {number}')]")
        self.ADDRESS = (By.XPATH, "//*[contains(text(),'Giovanni Rovelli')]/../td[4]")
        self.CONTACT_NAME = (By.XPATH, "//*[contains(text(),'Giovanni Rovelli')]")
        self.WR_CODE = (By.XPATH, "//*[contains(@class,'CodeMirror-code')]")

    def click_run_sql(self):
        self.wait_for_visibility(self.RUN_SQL)
        self.run_sql.click()
        return self

    def click_wr_code(self):
        self.switch_frame()
        self.wr_code.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        return self

    def insert_sql(self):
        """Ввод команды"""
        # self.clear_field(self.WR_CODE)
        self.clear_field(locator=self.WR_CODE, use_keyword_comb=True)
        return self

    def check_name_and_address(self):
        address = self.get_text_from_element(self.ADDRESS)
        name = self.get_text_from_element(self.CONTACT_NAME)
        assert address == "Via Ludovico il Moro 22" and name == "Giovanni Rovelli"
