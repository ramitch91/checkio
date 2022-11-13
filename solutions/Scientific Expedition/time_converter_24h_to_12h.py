"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you
see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Example:
time_converter('12:30') == '12:30 p.m.'
time_converter('09:00') == '9:00 a.m.'
time_converter('23:15') == '11:15 p.m.'

How it is used: For work with the different time formats.

Precondition :
'00:00' <= time <= '23:59'

Also interesting fact about "12:00 p.m." and "12:00 a.m.". The name of this fact is "Confusion at noon and midnight" -
problem using "p.m./ a.m." with this magical time "12:00". You can find information about this in Wikipedia or just
google it.
"""


import datetime

def time_converter(time):
    dtime = datetime.time(time)
    thour = int(dtime.hour)
    tminute = int(dtime.minute)
    print(thour, tminute)
    if thour <= 12:
        time = str(thour) + ':' + str(tminute) + ' a.m.'
    else:
        time = str(thour - 12) + ':' + str(tminute) + ' p.m.'
    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")