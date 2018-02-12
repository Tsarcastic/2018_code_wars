"""Find the number with the most digits."""

def find_longest(arr):
    most_dig = arr[0]
    for i in arr:
        if len(i) > len(most_dig):
            most_dig = i