import pandas as pd

def check_if_valid_data(df):
        """Check if a dataframe is empty.
                Args:
                df (pd.dataframe): The dataframe from respons.
                
                Returns:
                bool: True The dataframe is not empty.
        """

        if df.empty:
                print("No data downloaded. Finishing execution")
                return False
        return True
