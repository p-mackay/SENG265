#!/usr/bin/env python3

import datetime
from datetime import timedelta

def main():

    student = {'name': 'John','age': 25,'courses': ['Math', 'CSC']}
    print(student['courses'])

    student['courses'].append('ANTH')
    print(student['courses'])



if __name__ == "__main__":
    main()
