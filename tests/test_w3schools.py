def test_check_user(app):
    """
    Empty password.
    """

    app.training_sql.choice_table_customers()
    a=1
    # app.login_page.open_login_page()
    # username = "Aleppo"
    # password = None
    # app.login_page.entry_data(username=username, password=password)
    # assert app.login_page.log_in() == LoginMessages.LOG_IN