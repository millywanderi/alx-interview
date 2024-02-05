#!/usr/bin/python3
"""N Queens Problem"""

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = [] # coordinates format [row, column]
    stop = False
    row = 0
    col = 0

    # iterate through rows
    while row < n:
        goback = False
        #iterate through columns
        while col < n:
            # check if the current column is safe
            safe = True
            for cord in placed_queens:
                c = cord[1]
                if(c == col or c + (row-cord[0]) == col or
                        c - (row-cord[0]) == col):
                    safe = False
                    break
            
            if not safe:
                if col == n - 1:
                    goback = True
                    break
                col += 1
                continue

            # place queen
            cords = [row, col]
            placed_queens.append(cords)
            # if last row, append solution and reset all the last unfinished row
            # and last safe column in that row
            if row == n -1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        row = cord[0]
                        col = cord[1]
                for i in range(n - row):
                    placed_queens.pop()
                if row == n - 1 and col == n - 1:
                    placed_queens = []
                    stop = True
                row -= 1
                col += 1
            else:
                col = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if goback:
            row -= 1
            while row >= 0:
                col = placed_queens[row][1] + 1
                del placed_queens[row]  # delete previous queen coordinates
                if col < n:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
