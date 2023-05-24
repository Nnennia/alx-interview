#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
count = 0


def print_status():
    """Compute metrics"""
    print("File size: {}".format(total_size))
    for key, value in sorted(cache.items()):
        if value > 0:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        try:
            code = line.split()[-2]
            if code in cache.keys():
                cache[code] += 1
        except BaseException:
            pass

        try:
            size = line.split()[-1]
            total_size += int(size)
        except BaseException:
            pass

        # print metrics every 10 lines
        count += 1
        if (count % 10 == 0):
            print_status()

    print_status()

except KeyboardInterrupt:
    print_status()
    raise
