#!/usr/bin/
"""Pascal's Triangle"""
def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        pascal_list = []
        for i in range(n):
            temp_list = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    number = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
                    temp_list.append(number)
            pascal_list.append(temp_list)
        return pascal_list
