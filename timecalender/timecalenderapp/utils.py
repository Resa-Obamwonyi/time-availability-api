from typing import overload
import pytz
import holidays
import iso8601
from datetime import datetime, timezone


# function converts time data to utc
def convert_to_utc(time_slot):
    # get country code
    country_code = time_slot["CC"]
    # parse the time string into an acceptable formate, remove all white spaces
    from_time = iso8601.parse_date(time_slot["from"].replace(" ", ""))
    to_time = iso8601.parse_date(time_slot["to"].replace(" ", ""))
    # get location
    location = pytz.country_timezones[country_code][0]
    # print(location, from_time)

    # confirm if day is holiday or weekend in location before proceeding
    is_weekend = from_time.weekday() > 4
    is_holiday = holidays.country_holidays(country_code).get(from_time)

    if is_weekend:
        msg = f"It's a weekend in {location}"
        return msg

    if is_holiday:
        msg = f"It's a holiday in {location}"
        return msg

    # if not holiday or weekend, convert to utc and return the utc time slots
    dt_from = from_time.astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    dt_to = to_time.astimezone(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return [dt_from, dt_to]


# function gets overlapping time slots based on data provided
def get_overlapping_time(slot_array):
    # sort the time slots
    slot_array.sort()
    # get first time slot as base case
    overlap = [slot_array[0]]
    # loop through and update start time or end time based on comparisons below
    for interval in slot_array[1:]:
        # if base case start time is lesser or equal to interval start time which is lesser or equal to base case end time
        if overlap[-1][0] <= interval[0] <= overlap[-1][-1]:
            # update base case start time to new interval start time
            overlap[-1][0] = interval[0]

        # if base case end time is greater or equal to interval end time
        if overlap[-1][1] >= interval[1]:
            # update base case end time to new interval end time
            overlap[-1][1] = interval[1]

    # format response appropriately
    response = []
    for overlap_time in overlap:
        new_dict = {"from": overlap_time[0], "to": overlap_time[1]}
        response.append(new_dict)

    # return array of overlap
    return response
