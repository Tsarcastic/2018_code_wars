"""Find the number with the most digits."""

def find_longest(arr):
    #your code here
    most_dig = arr[0]
    for i in arr:
        if len(str(i)) > len(str(most_dig)):
            most_dig = i
    return most_dig