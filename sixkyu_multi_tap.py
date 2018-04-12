"""https://www.codewars.com/kata/54a2e93b22d236498400134b/train/python ."""

def presses(phrase):
    phrase = phrase.lower()
    return_sum = 0
    one_touch = ['a', 'd', 'g', 'j', 'm', 'p', 't', 'w', ' ', '1', '*', '#']
    two_touch = ['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x', '0']
    three_touch = ['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']
    four_touch = ['2', '3', '4', '5', '6', '8', 's', 'z']
    five_touch = ['7', '9']


    for letter in phrase:
        if letter in one_touch:
            return_sum += 1
        elif letter in two_touch:
            return_sum += 2
        elif letter in three_touch:
            return_sum += 3
        elif letter in four_touch:
            return_sum += 4
        elif letter in five_touch:
            return_sum += 5

    return return_sum


