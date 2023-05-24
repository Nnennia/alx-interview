#!/usr/bin/python3
"""A method to determine if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    if data == []:
        return True
    binary_data = [bin(num)[2:].zfill(8) for num in data]
    if binary_data[0][0:1] == "0":
        return True
    elif binary_data[0][0:3] == "110" \
            or binary_data[0][0:4] == "1110" and len(binary_data) >= 3 \
            or binary_data[0][0:5] == "11110" and len(binary_data) >= 4:
        for bin_num in binary_data[1:]:
            if bin_num[0:2] != "10":
                return False
        return True
    else:
        return False
