#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return none

    maria_wins = 0
    ben_wins = 0

    n = max(nums)
    sieve = [True for h in range(1, n + 1, 1)]
    sieve[0] = False
    for k, is_sieve in enumerate(sieve, 1):
        if k == 1 or not is_sieve:
            continue
        for s in range(k + k, n + 1, k):
            sieve[s - 1] = False

    for p, n in zip(range(x), nums):
        sieve_count = len(list(filter(lambda x: x, sieve[0: n])))
        ben_wins += sieve_count % 2 == 0
        maria_wins += sieve_count % 2 == 1

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return "Ben"
