#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""

import sys
cache = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def log_parsing():
    total_size = 0
    counter = 0

    def parse_line(line, cache):
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = int(line_list[-2])
            size = int(line_list[-1])
            if code in cache:
                cache[code] += 1
            return size
        return 0

    try:
        cache = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
        for line in sys.stdin:
            total_size += parse_line(line, cache)
            counter += 1

            if counter == 10:
                counter = 0
                print('File size: {}'.format(total_size))
                for key, value in sorted(cache.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
                cache = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    except Exception as err:
        pass

    finally:
        print('File size: {}'.format(total_size))
        for key, value in sorted(cache.items()):
            if value != 0:
                print('{}: {}'.format(key, value))
