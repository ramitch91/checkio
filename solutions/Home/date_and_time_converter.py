#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run date-and-time-converter

# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
# 
# 
# 
# Input:Date and time as a string
# 
# Output:The same date and time, but in a more readable format
# 
# Precondition:
# 0 <  day <= 31
# 0 <  month <= 12
# 1900 <  year <= 3000
# 0 <= hours < 24
# 0 <= minutes < 60
# 
# 
# END_DESCRIPTION

import datetime


def date_time(time: str) -> str:
    # replace this for solution

    # Get the datetime object of the string entered
    time_format = "%d.%m.%Y %H:%M"
    date_object = datetime.datetime.strptime(time, time_format)

    # Test hours to see if 1 or not
    if date_object.hour == 1:
        print_hours = 'hour'
    else:
        print_hours = "hours"

    # Test minutes to see if 1 or not
    if date_object.minute == 1:
        print_minutes = 'minute'
    else:
        print_minutes = "minutes"

    # Set the time string to a more readable format
    string_format = f"%-d %B %Y year %-H {print_hours} %-M {print_minutes}"
    time_string = datetime.datetime.strftime(date_object, string_format)

    return time_string


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
