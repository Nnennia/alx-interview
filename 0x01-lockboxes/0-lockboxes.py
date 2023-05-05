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
            if key < len(boxes):
                if key not in unlocked_boxes and key != box_num:
                    unlocked_boxes.append(key)
    return len(unlocked_boxes) == len(boxes)
