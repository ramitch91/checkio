#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run sun-angle

# Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from
# the surrounding nature. Programming won't help you with the fire and water, but when it comes to the information
# extraction - it might be just the thing you need.
# 
# Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises
# in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which
# means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input
# will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".
# 
# 
# 
# Input:The time of the day.
# 
# Output:The angle of the sun, rounded to 2 decimal places.
# 
# Precondition:
# 00:00 <= time <= 23:59
# 
# 
# END_DESC

from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    # replace this for solution
    # Pull the hours and minutes from the input
    hours = int(time[:2])
    minutes = int(time[3:])

    # Get total minutes for use in the calculations
    total_minutes = hours * 60 + minutes

    # Check to see if the time is before 06:00 or after 18:00. If so, return "I don't see the sun!"
    if total_minutes < 360 or total_minutes > 1080:
        return "I don't see the sun!"

    # Get the time difference in hours and multiply it by the total degrees the sun moves per hour
    time_diff = (total_minutes - 360) / 60
    angle = time_diff * 15
    return angle


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
