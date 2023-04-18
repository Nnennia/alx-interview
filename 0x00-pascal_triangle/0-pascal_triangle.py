#!/usr/bin/python3
"""Pascal's Triangle"""
def pascal_triangle(n):
    """Function that prints the pascal's triangle 
    where n is an integer and n is greater than 0"""
    if n <= 0:
        return [] # return empty list if n is less than or equal to 0
    else:
        pascal_list = []
        for i in range(n):
            temp_list = [] # a new temporary list to append the contents to the pascal list
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    number = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
                    temp_list.append(number)
            pascal_list.append(temp_list)
        return pascal_list
