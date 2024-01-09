#!/usr/bin/python3
"""
Unlocking boxes where each boxes contains a list
of keys that can open other boxes.
"""


def canUnlockAll(boxes):
    """Function that unlocks all boxes"""
    if not boxes or len(boxes) == 1:
        return True  # all boxes are considered opened

    # Keys initially contain the keys from the first box
    keys = set([0])

    # Track visited boxes
    visited = set([0])

    # Initialize the first box in the queue
    queue = [0]
    # Get the box at the front of the queue
    while queue:
        currBox = queue.pop(0)

        for key in boxes[currBox]:
            # check if the key is valid
            if key not in visited and key < len(boxes):
                keys.add(key)
                queue.append(key)
                visited.add(key)

    return len(keys) == len(boxes)
