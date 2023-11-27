from ui_elements.trysql_page import TrySQLPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.training_sql = TrySQLPage(self)

    def quit(self):
        self.driver.quit()
