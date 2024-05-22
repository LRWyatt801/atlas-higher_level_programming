#!/usr/bin/python3
"""Contains pascal_triangle function"""


def pascal_triangle(n: int) -> list:
    """Returns a list of lists of ints representing pascals triangle

    Args:
        n (int): Number of layers to return

    Returns:
        list: List of lists of integers represneting pascals triangle
    """
    
    # matrix to store generated values
    triangle = [[0 for x in range(n)]
                    for y in range(n)]
    
    # iterate through every line
    for line in range(0, n):
        
        # each line has number of int
        # equal to line number
        for i in range(0, line + 1):
            
            # firs and last values
            # in every row are 1
            if(i is 0 or i is line):
                triangle[line][i] = 1
            
            # calc new value
            else:
                triangle[line][i] = (triangle[line - 1][i - 1] + triangle[line - 1][i])
    
    return triangle
