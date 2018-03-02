"""https://www.codewars.com/kata/546a3fea8a3502302a000cd2/train/python."""


def find_the_ball(start, swaps):
    """Classic street con."""
    ball = start

    for i in swaps:
        if i[0] == ball:
            ball = i[1]
        elif i[1] == ball:
            ball = i[0]

    return ball
