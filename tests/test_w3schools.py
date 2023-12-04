def test_check_user(app):
    """
    Проверка полей ContactName и Address
    """
    (app.
     training_sql.
     click_run_sql().
     check_name_and_address())


def test_city(app):
    """
    Проверка записей в таблице
    """
    (app.
     training_sql.
     click_wr_code())
