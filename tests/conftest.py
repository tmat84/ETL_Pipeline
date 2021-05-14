import pytest
from database.config import config
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def params():
    return config(filename=os.path.join(BASE_DIR,"pytest.ini"))
