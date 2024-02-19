# Rotate 2D Matrix
This Python script provides a function to rotate an n x n 2D matrix by 90 degrees clockwise. The rotation is done in-place, meaning the original matrix is modified directly without using additional memory.

## Usage
To use the `rotate_2d_matrix` function, simply import it into your Python script and pass a 2D matrix as the argument. Here's an example:
'''python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)

This will output:
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]

## Function Description
The `rotate_2d_matrix` function takes a single argument:
* `matrix`: A non-empty n x n 2D list representing the matrix to be rotated.
* The function does not return anything. Instead, it directly modifies the input matrix in-place. 

## Requirements
* Python 3.x
