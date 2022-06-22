import pytz
from datetime import datetime

# function converts time data to gmt
def convert_to_utc(time_slot):
    country_code = time_slot['CC']
    from_time = time_slot['from']
    to_time = time_slot['to']
    timezone =  pytz.country_timezones[country_code]
    dt_from = pytz.timezone(timezone[0]).localize(datetime.strptime(from_time, '%Y-%m-%d %H:%M:%S')).astimezone(pytz.utc)
    dt_to = pytz.timezone(timezone[0]).localize(datetime.strptime(to_time, '%Y-%m-%d %H:%M:%S')).astimezone(pytz.utc)
    
    return {"utc":[country_code, dt_from, dt_to]}


# function gets the holidays in each country provided
def get_holidays(country):
    pass

# function gets overlapping time slots based on data provided
def get_overlapping_time():
    pass