#!/usr/bin/python3
"""Module containing:
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Funtion that finds the quotient of matirx / div

    Args:
        matrix (int, float): Numerator
        div (int, float): Denomenator

    Raises:
        TypeError: row size not equal error
        TypeError: type error in matrix, must be number
        TypeError: type error for div must be number
        ZeroDivisionError: div cannot be 0

    Returns:
        matrix: matrix of quotients
    """
    
    # checks for matrix
    first_row_len = len(matrix[0])
    for row in matrix:
        # check if all rows have the same length
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            # check if all elements in matrix are numbers
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    #checks for div
    if not isinstance(div, (int, float)):  # check div is int/float
        raise TypeError("div must be a number")
    elif div == 0:  # check division by 0
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with the same dimensions as input matrix
    new_matrix = [[0 for _ in range(first_row_len)]for _ in range(len(matrix))]
    # perform division
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round((matrix[i][j] / div), 2)
    return new_matrix
