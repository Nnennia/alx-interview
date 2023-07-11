#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix) -> None:
    """ Given an n x n 2D matrix, rotate it
    90 degrees clockwise.
    """
    temp = []  # initialize empty list
    for item in matrix:
        temps = []  # initialize empty inner list
        # print(f"First => {item}")
        for item in matrix:  # for each inner list
            elem = item.pop(0)  # pop it's first item
            temps.insert(0, elem)  # add it to the start of the list
            # print(f"Second => {item}")
            # print(temps)
        temp.append(temps)  # append to list to the mother list
    matrix.clear()  # reset/ clear the given list
    for item in temp:  # add all items back
        matrix.append(item)
