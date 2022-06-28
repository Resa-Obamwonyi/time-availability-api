import pytz
import holidays
import iso8601
from datetime import datetime, timezone


# function converts time data to utc
def convert_to_utc(time_slot):
    # get country code
    country_code = time_slot['CC']
    # parse the time string into an acceptable formate, remove all white spaces
    from_time = iso8601.parse_date(time_slot['from'].replace(" ", ""))
    to_time = iso8601.parse_date(time_slot['to'].replace(" ", ""))
    # get location
    location =  pytz.country_timezones[country_code]

    #confirm if day is holiday or weekend in location before proceeding
    is_weekend = from_time.weekday() > 4
    is_holiday = holidays.country_holidays(country_code).get(from_time)
    if is_weekend or is_holiday:
        return [None]

    #if not holiday or weekend, convert to utc and return the utc time slots
    dt_from = from_time.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    dt_to = to_time.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # print("\n \n", dt_from, dt_to)
    return [dt_from, dt_to]


# function gets the holidays in each country provided
def get_holidays(country):
    # get over_lapping time
    pass

# function gets overlapping time slots based on data provided
def get_overlapping_time(slot):
    pass