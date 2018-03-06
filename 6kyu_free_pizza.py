"""
https://www.codewars.com/kata/595910299197d929a10005ae/train/python .

In an attempt to boost sales, the manager of the pizzeria you work
at has devised a pizza rewards system: if you already made at least 5
orders of at least 20 dollars, you get a free 12 inch pizza with 3
toppings of your choice.

However, the rewards system may change in the future. Your manager wants
you to implement a function that, given a dictionary of customers, a
minimum number of orders and a minimum order value, returns a set of
the customers who are eligible for a reward.

Customers in the dictionary are represented as:

{ 'customerName' : [list_of_order_values_as_integers] }
"""


def pizza_rewards(customers, min_orders, min_price):
    """

    Who is eligible for the reward.

    Return a list of [customers] who have placed a minimum of [min_orders]
    at [min_price].
    """
    eligible_customers = []

    for customer in customers:
        eligible_orders = 0

        for order in customers[customer]:
            if order >= min_price:
                eligible_orders += 1

        if eligible_orders >= min_orders:
            eligible_customers.append(customer)

    return eligible_customers
