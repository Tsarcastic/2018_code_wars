"""

Buying a car.

https://www.codewars.com/kata/554a44516729e4d80b000012/train/python

"""
import math

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    """How many months it takes to get to the center of a tootsie pop."""

    currentPriceOld = startPriceOld
    currentPriceNew = startPriceNew

    savings = 0

    months = 0

    while currentPriceOld + savings < currentPriceNew:
        savings += savingperMonth

        currentPriceOld -= (currentPriceOld * (percentLossByMonth / 100))
        currentPriceNew -= (currentPriceNew * (percentLossByMonth / 100))

        if months % 2 == 0:
            percentLossByMonth += .5

        months += 1

    left_over = round(currentPriceOld) + math.ceil(savings) - math.ceil(currentPriceNew)
      

    return [months, left_over]