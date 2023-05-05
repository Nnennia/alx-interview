#!/usr/bin/python3
"""Lock boxes
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    unlocked_boxes = [0]
    for box_num in range(len(boxes)):
        if not boxes[box_num]:
            continue
        for key in boxes[box_num]:
            if key < len(boxes) and key not in unlocked_boxes and key != box_num:
                unlocked_boxes.append(key)
    return len(unlocked_boxes) == len(boxes)

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.

# boxes = [[1], [2], [3], [4], []]
# print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))

# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))