#!/usr/bin/env python3
"""
Pascal Triangle Generator
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's Triangle.
              Returns an empty list if n <= 0.
    """
    result = []
    if n <= 0:
        return result
    result = [[1]]
    for current_row in range(1, n):
        new_row = [1]
        for current_column in range(len(result[current_row - 1]) - 1):
            previous_row = result[current_row - 1]
            new_row.append(
                previous_row[current_column] + previous_row[current_column + 1]
            )
        new_row.append(1)
        result.append(new_row)
    return result
