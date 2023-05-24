#!/usr/bin/python3
"""A method to determine if a given data set represents a valid UTF-8 encoding"""
import re


def validUTF8(data):
    if data == []:
        return True
    binary_data = (bin(num)[2:].zfill(8) for num in data)
    if binary_data[0][0:1] == "0":
        return True
    elif re.match(r'^110[10]{6}$', binary_data[0]):
        if len(binary_data) >= 2 and all(re.match(r'^10[01]{7}$', num)
                                         for num in binary_data[1:2]):
            return True
    elif re.match(r'^1110[10]{4}$', binary_data[0]):
        if len(binary_data) >= 3 and all(re.match(r'^10[01]{7}$', num)
                                         for num in binary_data[1:3]):
            return True
    elif re.match(r'^11110[10]{3}$', binary_data[0]):
        if len(binary_data) >= 4 and all(re.match(r'^10[01]{7}$', num)
                                         for num in binary_data[1:4]):
            return True
    return False
