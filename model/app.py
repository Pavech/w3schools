from ui_elements import trysql_page


class Application:

    def __init__(self, webdriver):
        self.training_sql = trysql_page.TrySQLPage(webdriver)
