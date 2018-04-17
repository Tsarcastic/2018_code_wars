"""https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python ."""

import string


def is_pangram(s):
    the_list = []
    for letter in s.lower():
        if letter.isalpha() and letter not in the_list:
            the_list.append(letter)
    return len(the_list) == 26
