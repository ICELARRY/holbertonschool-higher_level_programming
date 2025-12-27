#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns a new matrix with the square of each value."""
    return [[value ** 2 for value in row] for row in matrix]
