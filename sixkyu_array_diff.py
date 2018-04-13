"""https://www.codewars.com/kata/523f5d21c841566fde000009/train/python ."""

def array_diff(a, b):
    return_array = []
    for num in a:
        if num not in b:
            return_array.append(num)

    return return_array