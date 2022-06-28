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
    # print(location, from_time)

    #confirm if day is holiday or weekend in location before proceeding
    is_weekend = from_time.weekday() > 4
    is_holiday = holidays.country_holidays(country_code).get(from_time)
    if is_weekend or is_holiday:
        return None

    #if not holiday or weekend, convert to utc and return the utc time slots
    dt_from = from_time.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    dt_to = to_time.astimezone(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # print("\n \n", dt_from, dt_to)
    return [dt_from, dt_to]

# function gets overlapping time slots based on data provided
def get_overlapping_time(slot_array):
    slot_array.sort()
    overlap = [slot_array[0]]
    for interval in slot_array[1:]: 
        if overlap[-1][0] < interval[0]:
            overlap[-1][0] = interval[0]
        elif overlap[-1][1] > interval[1]:
            overlap[-1][1] = interval[1]
        else:
            pass
        
    print("\n \n", overlap)
    
    # start_time = None
    # end_time = None
    # for slot in range(len(slot_array)):
    #     start_time =  slot_array[slot][0]
    #     end_time = slot_array[slot][1]

    #     if start_time:
    #         pass

#[['T01:00:00Z', 'T09:00:00Z'], =====> 1 - 9
# ['T08:00:00Z', 'T16:00:00Z'], =====> 8 - 16
# ['T03:30:00Z', 'T11:30:00Z']] =====> 3:30 - 11:30  |  8, 9