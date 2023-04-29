#!/usr/bin/python3
"""Lock boxes
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    unlocked_box = [0]
    for box_num, i in enumerate(boxes):
        if not i:
            continue
        for keys in i:
            if keys < len(boxes) and keys not in unlocked_box and keys != box_num:
                 unlocked_box.append(keys)
    if len(unlocked_box) == len(boxes):
        return True
    return False

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))