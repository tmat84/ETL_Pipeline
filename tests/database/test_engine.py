import pytest

from database.engine import postgresEngine


@pytest.xfail(reason="“Using TDD,is not implemented")
def test_connection(params):
    """Check the connection to local database """
    with postgresEngine(**params) as db:
        engine, connect = db
    
    sql_query = """
                    SELECT name 
                    FROM holidays
                    WHERE country = 'Poland' AND date = '2021-05-01'

    """
    data = connect.execute(sql_query).fetchone()
    assert data is not None
    # the data variable is a tuple
    assert data[0] == "Labor Day / May Day"
