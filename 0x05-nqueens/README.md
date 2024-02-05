# N-Queens Solver
This is a python program that solves the N-Queens problem, a classic chess puzzle where N non-attacking queens must be placed on an N*N chessboard. The program takes an integer `N`as a command-line argument and prints every possible solution to the problem.

## Usage
The program is run using the following command.
`python3 nqueens.py N`

Replace `N` with the desired size of the chessboard. The program will then print each solution on a separate line, adhering to the specified format.

## Error Handling
The program includes error handling for different scenarios:

1. If the user provides the wrong number of arguments:
`Usage: nqueens N`
Exit status: 1

2. If `N` is not an integer:
`N must be a number`
Exit status: 1

3. If `N` is smaller than 4:
`N must be at least 4`
Exit status: 1

## Implementation Details
* The program uses a backtracking algorithm to find solutions to the N-Queens problem.
* It checks for the correctness of the command-ine argument and handles errors accordingly.
