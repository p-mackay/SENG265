#!/usr/bin/env python3

import datetime
from datetime import timedelta


def init():
    return [(datetime.datetime(2020, 1, 20), datetime.datetime(2020, 3, 7)),
        (datetime.datetime(2020, 4, 18), datetime.datetime(2020, 5, 16)),
        (datetime.datetime(2020, 1, 1), datetime.datetime(2020, 5, 28)),
        (datetime.datetime(2020, 1, 22), datetime.datetime(2020, 2, 7)),
        (datetime.datetime(2020, 2, 10), datetime.datetime(2020, 4, 18)),
        (datetime.datetime(2020, 2, 21), datetime.datetime(2020, 6, 12)),
        (datetime.datetime(2020, 4, 2), datetime.datetime(2020, 6, 7)),
        (datetime.datetime(2020, 5, 16), datetime.datetime(2020, 5, 26)),
        (datetime.datetime(2020, 3, 19), datetime.datetime(2020, 4, 21)),
        (datetime.datetime(2020, 6, 3), datetime.datetime(2020, 6, 12))]


"""
The following won't work immediately as you must as first add
parameters to the function definition.
"""

def within_deadline(dt1, dt2, num_days):
    if dt1 > dt2:
        dt_buffer = dt1
        dt1 = dt2
        dt2 = dt_buffer
    
    dt3 = dt1 + timedelta(days=num_days)
    print(dt1, dt2, dt3)
    print(dt3 - dt2)

    if dt3 - dt2 <= timedelta(days=num_days):
        return True
    else:
        return False
        

    """
    The first parameter is a datetime, the second paramter is a
    datetime, and the first is guaranteed to be before the second 
    in time. The third parameter is the number of days corresponding
    to a "deadline". If the second datetime is within the deadline (that
    is, the first datetime + number of days), then return True; otherwise
    return False.
    """


def main():
    d1 = datetime.datetime(2020, 5, 16)
    d2 = datetime.datetime(2020, 5, 26)

    print(within_deadline(d1, d2, 14))


if __name__ == "__main__":
    main()
