"""https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python ."""

def two_sum(numbers, target):
    for b_counter, big in enumerate(numbers):
        for s_counter, small in enumerate(numbers):
            if target == big + small and b_counter != s_counter:
                return [b_counter, s_counter]

