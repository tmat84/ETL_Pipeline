from sqlalchemy import create_engine
import pyodbc
from contextlib import contextmanager

@contextmanager
def postgresEngine(user="postgres",password="password",host="localhost",database="etl_holiday"):
    """Produces the postgres engine and connect to postgres database.
        
        Args:
        user (str): the username used to authenticate.
        password (str): password used to authenticate.
        host (str): database server address e.g., localhost or an IP address.
        database (str): the name of the database that you want to connect.

        Returns:
        Object: The postgres engine and connection.
    """
    # set up database connection
    engine = create_engine("postgresql://{}:{}@{}/{}".format(user,
                                                            password,
                                                            host,
                                                            database))
    try:
        connect = engine.connect()
        yield engine, connect
    finally:
    #tear down database connection
        if connect is None: 
            connect.close()




