#!/usr/bin/python3
"""This module prints a pascal triangle"""


def pascal_triangle(n):
    """A function that prints pascal triangle"""
    if n <= 0:
        return []

    tr = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = tr[i - 1][j - 1] + tr[i - 1][j]
        tr.append(row)
    return tr
