from ui_elements.trysql_page import TrySQLPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.training_sql = TrySQLPage(self)

    def quit(self):
        self.driver.quit()
