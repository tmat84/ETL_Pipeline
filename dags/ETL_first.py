import pandas as pd
import requests
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from helpers.data_manipulation import custom_json_to_df
from helpers.data_validation import check_if_valid_data
from database.config import config
from database.engine import postgresEngine
from sqlalchemy import create_engine
from datetime import date

# https://calendarific.com/api-documentation

def ETL_first():
    """
    Runs the ETL pipeline monthly on the docker locally. 
    
    """
    params = config(section="api")
    month = date.today().month
    try:
        resp = requests.get(
        "https://calendarific.com/api/v2/holidays?\
        api_key={token}&\
        country=PL&\
        year=2021&month={month}}".format(token=params["token"],month=month)
        )
        resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

    data = resp.json()

    holiday_df = custom_json_to_df(data)

    if check_if_valid_data(holiday_df):
        print("Valid data")
    else:
        raise Exception("Empty dataframe")
    
    # get prarams for postgresql
    params = config(filename='database\database.ini',section='postgresql')
    #The db ip address of container  
    with postgresEngine(**params) as db:

        engine,connect = db
        sql_query = """
        CREATE TABLE IF NOT EXISTS holidays(
            name VARCHAR(200),
            description VARCHAR(255),
            country VARCHAR(200),
            date VARCHAR(200),
            holiday_type VARCHAR(200),
            PRIMARY KEY (country,date)
            )
        """
        connect.execute(sql_query)

        # cur.execute(sql_query)
        # conn.commit()

        try:
            holiday_df.to_sql("holidays", engine, index=False, if_exists='append')
        except Exception as e:
            print(e)
            print("Data already exists in the database")

        
        print("Close database successfully")
