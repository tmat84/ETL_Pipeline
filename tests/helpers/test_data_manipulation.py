import pytest
import pandas as pd
import json
from helpers.data_manipulation import custom_json_to_df
import os
import pytest
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def respons_json():
    with open(os.path.join(BASE_DIR,"input_data.json"),encoding='utf-8') as f:
        return json.load(f)

@pytest.fixture
def df():
    return pd.read_json(os.path.join(BASE_DIR,"normalized_data.json"),
                        encoding='utf-8',
                        convert_dates=False)
                        

def test_column_number(respons_json,df):
    actual_df = custom_json_to_df(respons_json)
    actual_df = sorted(list(actual_df.columns))
    expected_df = sorted(list(df.columns))
    message = (f"test_column_number(respons_json,df) returned {actual_df} instead of {expected_df}")
    assert actual_df == expected_df,message


def test_row_number(respons_json,df):
    actual_df = custom_json_to_df(respons_json)
    actual_df = len(actual_df)
    expected_df = len(df)
    message = (f"test_name_column_value(respons_json,df) returned {actual_df} instead of {expected_df}")
    assert actual_df == expected_df,message


def test_date_column_value(respons_json,df):
    actual_df = custom_json_to_df(respons_json)
    actual_df = actual_df.loc[0,"date"]
    expected_df = df.loc[0,"date"]
    message = (f"test_name_column_value(respons_json,df) returned {actual_df} instead of {expected_df}")
    assert actual_df == expected_df,message


def test_name_column_value(respons_json,df):
    actual_df = custom_json_to_df(respons_json)
    actual_df = actual_df.loc[0,"name"]
    expected_df = df.loc[0,"name"]
    message = (f"test_name_column_value(respons_json,df) returned {actual_df} instead of {expected_df}")
    assert actual_df == expected_df,message

