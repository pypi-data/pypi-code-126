from ovretl.performances_utils.calculate_business_hours_delta import calculate_business_hours_delta
import datetime
import pandas as pd


def test_calculate_business_hours_delta():
    date_1 = pd.to_datetime(datetime.datetime(2020, 6, 26, 15, 45))
    date_2 = pd.to_datetime(datetime.datetime(2020, 6, 29, 9, 30))
    assert calculate_business_hours_delta(date_1, date_2) == 2.75

    date_3 = pd.to_datetime(datetime.datetime(2020, 6, 25, 15, 30))
    date_4 = pd.to_datetime(datetime.datetime(2020, 6, 26, 9, 30))
    assert calculate_business_hours_delta(date_3, date_4) == 3.0

    date_5 = pd.to_datetime(datetime.datetime(2020, 6, 25, 9, 30))
    date_6 = pd.to_datetime(datetime.datetime(2020, 6, 26, 15, 30))
    assert calculate_business_hours_delta(date_5, date_6) == 15.0

    date_7 = pd.to_datetime(datetime.datetime(2020, 6, 25, 9, 45))
    date_8 = pd.to_datetime(datetime.datetime(2020, 6, 25, 15, 30))
    assert calculate_business_hours_delta(date_7, date_8) == 5.75

    date_9 = pd.to_datetime(datetime.datetime(2020, 6, 25, 15, 30))
    date_10 = pd.to_datetime(datetime.datetime(2020, 6, 27, 19, 30))
    assert calculate_business_hours_delta(date_9, date_10) == 9.5

    date_11 = pd.to_datetime(datetime.datetime(2020, 6, 26, 15, 30))
    date_12 = pd.to_datetime(datetime.datetime(2020, 6, 30, 9, 30))
    assert calculate_business_hours_delta(date_11, date_12) == 12.0

    date_13 = pd.to_datetime(datetime.datetime(2020, 6, 28, 20, 30))
    date_14 = pd.to_datetime(datetime.datetime(2020, 6, 29, 10, 30))
    assert calculate_business_hours_delta(date_13, date_14) == 3.5

    date_15 = pd.to_datetime(datetime.datetime(2020, 8, 22, 17, 30))
    date_16 = pd.to_datetime(datetime.datetime(2020, 8, 25, 8, 30))
    assert calculate_business_hours_delta(date_15, date_16) == 10.5
