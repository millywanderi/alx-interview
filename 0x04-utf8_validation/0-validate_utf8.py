#!/usr/bin/python3
"""
Module that validates UTF-8
"""


def validUTF8(data):
    """A function that validates UTF-8
    """
    bytes_num = 0

    for num in data:
        if bytes_num == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                bytes_num = 1
            elif (num >> 4) == 0b1110:
                bytes_num = 2
            elif (num >> 3) == 0b11110:
                bytes_num == 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            bytes_num -= 1
    return bytes_num == 0
