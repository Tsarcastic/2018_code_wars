"""Count the number of each unique element in an array."""


def count(array):
    """."""
    count_dict = {}
    for i in array:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    return count_dict
