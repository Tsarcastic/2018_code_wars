"""

John has between m and n money.

He will always buy 9 cars and have 1 money left over.
He will always buy 7 boats and have 2 money left over.

For each range return a big list containing small lists where
["M: amount_of_money", "B: cost_of_boat, "C: cost_of_car"]

"""


def howmuch(m, n):
    """."""
    possible_answers = []

    for number in range(m, n):
        if number % 7 == 2 and number % 9 == 1:
            this_answer = []
            this_answer.append("M: {}".format(number))
            this_answer.append("B: {}".format(int(number / 7)))
            this_answer.append("C: {}".format(int(number / 9)))
            possible_answers.append(this_answer)

    return possible_answers
