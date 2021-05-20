import pandas as pd

def custom_json_to_df(data):
    """ Creates a pandas df from json.

        Args:
        data (str): The json data. 

        Returns:
        DataFrame: The df with columns:"date", "name",
         "holiday_type","country","description
    """
    name = []
    description = []
    country = []
    date = []
    holidayType = []

    for holiday in data["response"]["holidays"]:
        name.append(holiday["name"])
        description.append(holiday["description"])
        country.append(holiday["country"]["name"])
        date.append(holiday["date"]["iso"])
        holidayType.append(holiday["type"][0])

    holiday_dict = {
        "name":name,
        "description":description,
        "country":country,
        "date":date,
        "holiday_type":holidayType
    }

    holiday_df = pd.DataFrame(holiday_dict,
                              columns=[
                                  "date", "name", "holiday_type",
                                   "country","description"
                                   ]
                            )
    return holiday_df