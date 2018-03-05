"""https://www.codewars.com/kata/5884b6550785f7c58f000047/train/python"""

def group(arr):
    ret_array = []

    for n in arr:
        new_number = True

        for sub_list in ret_array:
            if n in sub_list:
                sub_list.append(n)
                new_number = False

        if new_number == True:
            new_num_list = [n]
            ret_array.append(new_num_list)

    return ret_array
