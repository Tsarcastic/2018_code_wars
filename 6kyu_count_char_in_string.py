"""https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python."""

def count(string):
    return_dict = {}

    for i in string:
        if i not in return_dict:
            return_dict[i] = 1
        else:
            return_dict[i] += 1

    return return_dict