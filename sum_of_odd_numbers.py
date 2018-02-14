"""

Given a triangle of consecutive odd numbers.

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

"""

def row_sum_odd_numbers(n):
    if n == 1:
        return n

    row_number = 2 
    value = 3

    while row_number < n:
        for x in range(row_number):
            value += 2
        row_number += 1

    ret_value = 0

    for x in range(row_number):
        ret_value += value
        value += 2

    return ret_value



