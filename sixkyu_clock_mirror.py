"""https://www.codewars.com/kata/56548dad6dae7b8756000037/train/python ."""


def what_is_the_time(time_in_mirror):
    time_in_mirror.split(":")

    first = int("{}{}".format(time_in_mirror[0], time_in_mirror[1]))
    second = int("{}{}".format(time_in_mirror[3], time_in_mirror[4]))

    first = 6 - (first - 6)
    if second != 0:
        first += -1
    if first == 0:
        first = 12
    if first == -1:
        first = 11

    minute = 30 - (second - 30)
    if minute == 60:
        minute = 0

    return '{:02d}:{:02d}'.format(first, minute)

"""

Best solution

def what_is_the_time(time_in_mirror):
    array = time_in_mirror.split(":")
    a = int(array[0])
    b = int(array[1])
    
    if a == 11: a = 12
    elif a == 12: a = 11
    else: a = 11 - a
    
    if b == 0: 
        b = 0
        a += 1
    else: b = 60 - b 
    return "{:02}:{:02}".format(a, b)

"""
