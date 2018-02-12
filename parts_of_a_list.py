"""https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python."""

"""def partlist(arr):
    new_arr = []
    for x in range(1,len(arr)):
        y = ' '.join(arr[:x])
        z = ' '.join(arr[x:])
        new_arr.append((y,z))
    return new_arr"""

def partlist(arr):
    """Divide a list into all the different, in order, permutations of two lists."""
    the_length = len(arr)
    big_timer = 0
    the_return = []
    while big_timer < the_length - 1:
        sub_list = []
        first_string = arr[0]
        little_timer = 1

        while little_timer <= big_timer:
            first_string += " " + arr[little_timer]
            little_timer += 1
        sub_list.append(first_string)

        second_string = arr[little_timer]
        little_timer += 1

        while little_timer < the_length:
            second_string += " " + arr[little_timer]
            little_timer += 1
        sub_list.append(second_string)

        ret_tup = (first_string, second_string)
        the_return.append(ret_tup)
        del ret_tup

        big_timer += 1

    return the_return
