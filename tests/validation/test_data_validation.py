#import unittest
import pytest
import pandas as pd
from helpers.data_validation import check_if_valid_data

#class Test_check_if_valid_data(unittest.TestCase):

@pytest.fixture
def df():
        return pd.DataFrame([(1,2),(3,4)],columns=["A","B"])

def test_empty_dataframe():
        actual = check_if_valid_data(pd.DataFrame())
        expected = False
        message = (f"check_if_valid_data(pd.DataFrame()) returned {actual} instead of {expected}")
        assert actual is expected, message


def test_dataframe_with_data():
        actual = check_if_valid_data(pd.DataFrame([(1,2),(3,4)],columns=["A","B"]))
        expected = True
        message = (f"check_if_valid_data(pd.DataFrame([(1,2),(3,4)],columns=[\"A\",\"B\"])) returned {actual} instead of {expected}")
        assert actual is expected, message



