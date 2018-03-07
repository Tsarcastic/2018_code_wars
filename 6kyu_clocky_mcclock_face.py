"""https://www.codewars.com/kata/59752e1f064d1261cb0000ec/train/python ."""

def what_time_is_it(angle):
    """Only the big hand"""

    rounded = round(angle)

    if angle < 30:
        hours = 12
    else:
        hours = str(int(rounded / 30)).zfill(2)

    minutes = int((angle % 30) / .5).zfill(2) 

    return '{}:{}'.format(hours, minutes)