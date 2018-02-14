"""

Find the balance.

https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python

"""

def balance(left, right):
    """Find the balance of left and right."""

    def weigh(side):
        """Find the weight of each side."""
        weight = 0
        for i in side:
            if i == "!":
                weight += 2
            if i == "?":
                weight += 3
        return weight

    left_weight = weigh(left)
    right_weight = weigh(right)

    if left_weight > right_weight:
        return "Left"
    elif right_weight > left_weight:
        return "Right"
    else:
        return "Balance"

