#!/usr/bin/python3
"""
Module for Making Change
"""


def makeChange(coins, total):
    """
    A method that determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Sort the coins in decreasing order
    coins.sort(reverse=True)

    coin_count = 0

    # Iterate through each coin in the list of coins
    for coin in coins:
        if coin > total:
            continue

        # Calculate the number of times the current coin can be used
        count = total // coin

        # Update the total by subtracting the value of the coins used
        total -= count * coin

        # Update the total by adding the value of the coins used
        coin_count += count
        if total == 0:
            break

    # If we couldn't make change for the total, return -1
    if total > 0:
        return -1
    return coin_count
