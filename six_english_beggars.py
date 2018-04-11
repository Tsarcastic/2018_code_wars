"""https://www.codewars.com/kata/59590976838112bfea0000fa/train/python ."""


def beggars(values, n):
    the_return = []
    tracker = 0

    if n == 0:
        return the_return

    for beggar in range(n):
        the_return.append(0)

    while values:
        if tracker == n:
            tracker = 0
        the_return[tracker] += values.pop(0)
        tracker += 1

    return the_return
