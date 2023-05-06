#!/usr/bin/python3
"""Minimum Operators"""


def minOperations(n: int) -> int:
    """Return the minimum number of operations to
    reach 'n' using copy and paste."""
    if n <= 1:
        return 0
    count = 0
    copied = 0
    pasted = 1
    while pasted < n:
        if copied == 0:
            copied = pasted
            pasted += copied
            count += 2
        elif n - pasted > 0 and (n - pasted) % pasted == 0:
            copied = pasted
            pasted += copied
            count += 2
        elif copied > 0:
            # paste
            pasted += copied
            count += 1
    return count
