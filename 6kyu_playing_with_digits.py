"""https://www.codewars.com/trainer/python ."""


def dig_pow(n, p):
    digit_table = []
    check_sum = 0

    for number in str(n):
        digit_table.append(int(number))

    for digit in digit_table:
            check_sum += digit ** p
            p += 1

    if check_sum % n == 0:
        return check_sum / n
    else:
        return -1


