# Lockboxes

This is a python task that uses 'canUnlockAll' fuction to determine if all boxes can be opened, considering that each box may contain keys to other boxes.

## Description

Given a list of lists ('boxes'), where each inner list represents the keys within a box:
* A key with the same number as a box opens that box.
* All keys are positive integers.
* There can be keys that do not correspond to any box.
* The first box ('boxes[0]') is unlocked.

The function uses a breadth-first search (BFS) algorithm to traverse throught the boxes, collecting keys and tracking visited boxes. It returns 'True' if all boxes can be opened, otherwise 'False'.
