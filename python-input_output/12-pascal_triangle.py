#!/usr/bin/python3
"""
12-pascal_triangle.py
Generate Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): Number of rows

    Returns:
        list: Pascal's triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # First element of the row is always 1

        # Middle elements are sum of two elements above
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
