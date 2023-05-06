#!/usr/bin/python3
"""Minimum Operators"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to
    reach 'n' using copy and paste."""
    pasted = 1
    count = 0
    copied = 0
    while n > 1:
        if copied == 0:
            copied = pasted
            pasted += copied
            count += 2
        elif (n - pasted) % pasted == 0:
            copied = pasted
            pasted += copied
            count += 2
        else:
            pasted += copied
            count += 1
    return count


print(minOperations(9))
