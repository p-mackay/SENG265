class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
import math
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def delta_x(self, dx):
        return Point(self.x+dx, self.y)

    def delta_y(self, dy):
        return Point(self.x, self.y+dy)

    def translate(self, dx, dy):
        return Point(self.x+dx, self.y+dy)

class Circle:

    '''Accepts a CENTER POINT 
    and a RADIUS'''
    def __init__(self, Point , r = 0):
        self.Point = Point
        self.r = r
    def __repr__(self):
        return "Circle(%r, %r)" % (self.Point, self.r)

    def area(self):
        return ((math.pi)*self.r*self.r)

    def perimeter(self):
        return (2*(math.pi)*self.r)

    def translate(self, dx, dy):
        return Circle(Point(dx, dy), self.r)

#!/usr/bin/env python3
from geometry import Circle
from geometry import Point
import math

def main():
    p1 = Point(10,10)
    c1 = Circle(p1, 3)
    a = c1.area()
    b = c1.perimeter()

    print(c1)
    print(a)
    print(b)



if __name__ == "__main__":
    main()
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def delta_x(self, dx):
        return Point(self.x+dx, self.y)

    def delta_y(self, dy):
        return Point(self.x, self.y+dy)

    def translate(self, dx, dy):
        return Point(self.x+dx, self.y+dy)
#!/usr/bin/env python3
from geometry import Point

def main():

    p1 = Point()
    p2 = Point(3, 4)
    p3 = Point(-12.2, 101)
    p1

    p2
    p3
    li = [p3, Point(3)]
    li
    p4 = p1.delta_x(10)
    p5 = p1.delta_y(-10)
    p4

    p5
    p1
    p4 = p1.translate(5, -5)
    p4
    li2 = [p.translate(-3.4, 2.1) for p in li]
    li2

if __name__ == "__main__":
    main()
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

    if abs(dt3 - dt2) <= timedelta(days=num_days):
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
    data = init()
    white_space = ""
    for (d1, d2) in data:
        print(white_space, end="")

        print(d1)
        print(d2)
        if within_deadline(d1, d2, 14):
            print("Dates ARE within 14 days of each other")

            # Modify this line with a suitable call to
            # strftime().
            #
            # |||||||||||||||||||||||||||||||
            # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
            print (d1.strftime("The first date is a %A"))
        else:
            print("Dates are NOT within 14 days of each other")
        
        white_space = "\n"


if __name__ == "__main__":
    main()
import math
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def delta_x(self, dx):
        return Point(self.x+dx, self.y)

    def delta_y(self, dy):
        return Point(self.x, self.y+dy)

    def translate(self, dx, dy):
        return Point(self.x+dx, self.y+dy)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Circle:

    '''Acceptsself.aCENTER POINT 
    andself.aRADIUS'''
    def __init__(self, Point , r = 0):
        self.Point = Point
        self.r = r
    def __repr__(self):
        return "Circle(%r, %r)" % (self.Point, self.r)

    def area(self):
        return ((math.pi)*self.r*self.r)

    def perimeter(self):
        return (2*(math.pi)*self.r)

    def translate(self, dx, dy):
        return Circle(Point(dx, dy), self.r)

class Rectangle:
    
    def __init__(self, upper_right , lower_left):
        self.upper_right = upper_right
        self.lower_left = lower_left

    def __repr__(self):
        return "Rectangle(%r, %r)" % (self.upper_right, self.lower_left)

    def op(self, a, b):
        self.a = a
        self.b = b

        if self.a > 0 and self.b > 0:
            if self.a > self.b:
                return self.a - self.b
            else:
                return self.b - self.a

        elif self.a < 0 and self.b < 0:
            if abs(self.a) > abs(self.b):
                return abs(self.a) - abs(self.b)
            else:
                return abs(self.b) - abs(self.a)

        else:
            return abs(self.a) + abs(self.b)


    def area(self):
        a = self.upper_right.get_x()
        b = self.lower_left.get_x()
        c = self.upper_right.get_y()
        d = self.lower_left.get_y()

        return (self.op(a,b)*self.op(c,d))
            


    def perimeter(self):
        a = self.upper_right.get_x()
        b = self.lower_left.get_x()
        c = self.upper_right.get_y()
        d = self.lower_left.get_y()
        
        return 2*(self.op(a,b)+self.op(c,d))

    def translate(self, dx, dy):
        a = self.upper_right.get_x()
        b = self.lower_left.get_x()
        c = self.upper_right.get_y()
        d = self.lower_left.get_y()

        return Rectangle(Point(a + dx, c + dy), Point(b + dx, d + dy))




#!/usr/bin/env python3
from geometry import Circle
from geometry import Point
from geometry import Rectangle 
import math
import random

def main():

    p1 = Point(random.randrange(-10, 10), random.randrange(-10, 10))
    p2 = Point(random.randrange(-10, 10), random.randrange(-10, 10))
    print(p1)
    print(p2)
    s1 = Rectangle(p1, p2)
    print(s1)

    a = p1.get_x()
    b = p2.get_x()
    c = p1.get_y()
    d = p2.get_y()

    print(s1.area())
    print(s1.perimeter())


if __name__ == "__main__":
    main()
import math
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def delta_x(self, dx):
        return Point(self.x+dx, self.y)

    def delta_y(self, dy):
        return Point(self.x, self.y+dy)

    def translate(self, dx, dy):
        return Point(self.x+dx, self.y+dy)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Circle:

    '''Acceptsself.aCENTER POINT 
    andself.aRADIUS'''
    def __init__(self, Point , r = 0):
        self.Point = Point
        self.r = r
    def __repr__(self):
        return "Circle(%r, %r)" % (self.Point, self.r)

    def area(self):
        return ((math.pi)*self.r*self.r)

    def perimeter(self):
        return (2*(math.pi)*self.r)

    def translate(self, dx, dy):
        return Circle(Point(dx, dy), self.r)

class Rectangle:
    
    def __init__(self, upper_right , lower_left):
        self.upper_right = upper_right
        self.lower_left = lower_left

    def __repr__(self):
        return "Rectangle(%r, %r)" % (self.upper_right, self.lower_left)

    def op(self, a, b):
        self.a = a
        self.b = b

        if self.a > 0 and self.b > 0:
            if self.a > self.b:
                return self.a - self.b
            else:
                return self.b - self.a

        elif self.a < 0 and self.b < 0:
            if abs(self.a) > abs(self.b):
                return abs(self.a) - abs(self.b)
            else:
                return abs(self.b) - abs(self.a)

        else:
            return abs(self.a) + abs(self.b)


    def area(self):
        a = self.upper_right.get_x()
        b = self.lower_left.get_x()
        c = self.upper_right.get_y()
        d = self.lower_left.get_y()

        return (self.op(a,b)*self.op(c,d))
            


    def perimeter(self):
        a = self.upper_right.get_x()
        b = self.lower_left.get_x()
        c = self.upper_right.get_y()
        d = self.lower_left.get_y()
        
        return 2*(self.op(a,b)+self.op(c,d))

    def translate(self, dx, dy):
        a = self.upper_right.get_x()
        b = self.lower_left.get_x()
        c = self.upper_right.get_y()
        d = self.lower_left.get_y()

        return Rectangle(Point(a + dx, c + dy), Point(b + dx, d + dy))




#!/usr/bin/env python3

import sys

def main():

   print(sys.argv)


if __name__ == "__main__":
    main()
#!/usr/bin/env python
"""Paul MacKay - V00967869"""

import sys

def sort(words):
    print("\n")
    uniq = list(set(words))
    print("Unique words: ", uniq, "\n")

    alph = sorted(uniq)
    print("Sorted alphabetically: ", alph, "\n")
    
    longest = max(uniq, key=len)
    print("Longest word: ", longest, "\n")

    shortest = min(uniq, key=len)
    print("Shortest word: ", shortest, "\n")
    print("List of all words: ", words, "\n")


def main():
    if len(sys.argv) < 2:
        print("usage:", sys.argv[0], "'some,string,with,words'")
        sys.exit(1)

    f = open(sys.argv[1], "rt")

    line = list(f)
    line = ''.join(line)
    word = line.split(",")
    
    sort(word)

    f.close()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import sys

# TODO: Complete this function
def pythag(side_a, side_b):
    return -1

def main():
    if len(sys.argv) < 3:
        print("usage:", sys.argv[0], "<length> <length")
        sys.exit(1)

   # TODO: Complete the code HERE


if __name__ == "__main__":
    main()
#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) < 3:
        print("Need two lengths")
        sys.exit(0)

    a = float(sys.argv[1])
    b = float(sys.argv[2])

    c = (a ** 2 + b ** 2) ** 0.5
    print(c)


if __name__ == "__main__":
    main()
#!/usr/bin/env python

def main():
    # ??
    print("Nuttin' honey!")

    a = "12345"
    print("a is a string:", a)

    i = int(a)
    print("i is an int:", i)

    f = int(a)
    printf("f is a float:", f)


if __name__ == "__main__":
    main()
#!/usr/bin/env python

import sys

def main():
    if (len(sys.argv) == 1):
        print("Hello, whoever you are!")
    else:
        print("Hello,", sys.argv[1])

if __name__ == "__main__":
    main()
#!/usr/bin/env python3


# TODO: Complete this function
def pythag(side_a, side_b):
    return -1


def main():
    print("Sides %.3f and %.3f, hypotenuse %.4f" 
        % (10, 13, pythag(10, 13)) )

    print("Sides %.3f and %.3f, hypotenuse %.4f" 
        % (21.9, 31.2, pythag(21.9, 31.2)) )

    print("Sides %.3f and %.3f, hypotenuse %.4f" 
        % (719.21, 21.2, pythag(719.21, 21.2)) )


if __name__ == "__main__":
    main()
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

    if abs(dt3 - dt2) <= timedelta(days=num_days):
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
    data = init()
    white_space = ""
    for (d1, d2) in data:
        print(white_space, end="")

        print(d1)
        print(d2)
        if within_deadline(d1, d2, 14):
            print("Dates ARE within 14 days of each other")

            # Modify this line with a suitable call to
            # strftime().
            #
            # |||||||||||||||||||||||||||||||
            # VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
            print (d1.strftime("The first date is a %A"))
        else:
            print("Dates are NOT within 14 days of each other")
        
        white_space = "\n"


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import datetime
from datetime import timedelta

def main():
    """
    Create a datetime object for today's date
    """

    # COMPLETE IMPLEMENTATION
    todays_date = datetime.datetime(2022, 3, 4) 

    date_list = every_lab(todays_date)

    for date in date_list:
        print(date.strftime("%a, %d %b %y"))

    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 15 Jan 21"
    """

    # COMPLETE IMPLEMENTATION

    


def every_lab(todays_date):
    end_date = datetime.datetime(2022, 4, 8)
    labs = []
    this_lab = todays_date
    labs.append(this_lab)

    while this_lab < end_date:
       this_lab += timedelta(weeks=1) 
       labs.append(this_lab)
    
    return labs

    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """

    # COMPLETE IMPLEMENTATION


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import datetime
import sys

def main():
    """florence_sched.txt contains a list of dates and times 
       when patients need medications

       * There are 3 nurse available on duty. 
       * Florence works from 8:00:00 hrs to 15:59:59 hrs
       * Dana works from 16:00:00 hrs to 23:59:59 hrs
       * Sam works from 00:00:00 hrs to 7:59:59 hrs

       15:59:59 hours is in format hour:minute:second

       Read the file florence_schedule by piping at the command line, 
       using the command:

       ./q_care_schedule.py < florence_sched.txt

       The output is a printout of the sorted care schedule for each nurse.

       See file care_sched_nurses.txt to see what the output should 
       look like.

       HINT: You may use the datetime.time to compare hours of work 
       with medication requirement timings. 
    """

    # COMPLETE IMPLEMENTATION

if __name__ == "__main__":
    main()



#!/usr/bin/env python3

import datetime
from datetime import timedelta

def main():
    """
    Florence is a nurse in a clinic. She is caring for 4 patients on
    different medication schedules

    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours

    Starting with your current day and time, make a care schedule
    for the next 14 days that Florence can use to schedule
    who needs medication at what time.

    HINT: Create datetime objects for all times. Convert to ical
    and then sort. Now convert back to datetime objects to print out
    the final schedule.

    Follow the steps provided.

    STEP 1: Use function patient_schedule to get a list of
    medication times for every patient
    medication times in the list are in ical format

    mark_schedule = <...........COMPLETE..................>
    susan_schedule = <...........COMPLETE..................>
    chloe_schedule = <...........COMPLETE..................>
    alexander_schedule = <...........COMPLETE..................>


    STEP 2: Combine all the lists and then form a master list of
    when medication is required by which patient.

    Print the medication schedule sorted by time in the format below:

      Friday, 25 03 2021, 09:24:27 Time to give medication to Alexander
      Friday, 25 03 2021, 10:24:27 Time to give medication to Chloe

    Refer to florence_sched.txt to see what the final output
    should look like. You are not required to write this information
    to a file. Simply output to console is enough.

    HINT: You will need to keep track of who needs medication when.
    One way of doing this is with a dictionary. You may choose to
    use other ways.
    """

    # COMPLETE YOUR IMPLEMENTATION
    this_list = []
    dates = []
    merged = {}
    m_list = patient_schedule('Mark', 5)
    s_list = patient_schedule('Susan', 3)
    c_list = patient_schedule('Chloe', 8)
    a_list = patient_schedule('Alexander', 10)


    '''
    for time in m_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), m_list['name'])
    for time in s_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), s_list['name'])
    for time in c_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), c_list['name'])
    for time in a_list['times']:
        print(time.strftime('%A, %d %m %Y, %X'), a_list['name'])
    '''
    this_list.append(m_list)
    this_list.append(s_list)
    this_list.append(c_list)
    this_list.append(a_list)

    m_list = []

    for ele in this_list:
        for date in ele['times']:
            dates.append(date)

    dates.sort()
    for date in dates:
        

def patient_schedule(name, med_interval):
    """
    This function will take a patient name and corresponding
    medication interval and return a list of times when the patient needs
    medication, in ical format.  The function should use datetime_to_ical
    function.
    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours
    """
    patient = {'name' : name, 'times' : []} 
    end_date = datetime.datetime(2022, 3, 22)
    todays_date = datetime.datetime.today()
    tm = todays_date

    while tm < end_date:
        tm += timedelta(hours=med_interval)  
        patient['times'].append(tm)

    return patient



def generate_dates():
    date_list = []

    end_date = datetime.datetime(2022, 3, 22)
    todays_date = datetime.datetime.today()
    date = todays_date

    while date < end_date:
        date += timedelta(days=1)
        date_list.append(date) 

    return date_list


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import datetime


def init():
    result = [datetime.datetime(1971, 12, 25),
        datetime.datetime(1980, 7, 26),
        datetime.datetime(1954, 7, 17),
        datetime.datetime(1953, 6, 15),
        datetime.datetime(1946, 6, 14),
        datetime.datetime(1964, 6, 19),
        datetime.datetime(1977, 12, 21),
        datetime.datetime(1952, 10, 7),
        datetime.datetime(1955, 3, 21),
        datetime.datetime(1985, 11, 16),
        datetime.datetime(1961, 2, 24),
        datetime.datetime(1962, 7, 21),
        datetime.datetime(1956, 8, 31),
        datetime.datetime(1954, 9, 21),
        datetime.datetime(1966, 4, 28),
        datetime.datetime(1954, 2, 12),
        datetime.datetime(1979, 1, 18),
        datetime.datetime(1964, 8, 8),
        datetime.datetime(1961, 3, 8),
        datetime.datetime(1977, 11, 19)
    ]

    return result    


def before(list_dates, year, month, day):
    dt = datetime.datetime(year, month, day)
    dt_list = []

    for date in list_dates:
        if date < dt:
            dt_list.append(date)
    """
    Given a list of datetimes along with a year, month, and day
    as integers, return the list of all datetimes that are before
    that year/month/day.
    """
    return dt_list


def main():
    birthdates = init()

    # All birthdates before March 1, 1960

    older = before(birthdates, 1960, 3, 1)

    for d in older:
        print(d)


if __name__ == "__main__":
    main()
s1 = "2020-04-19"
s2 = "The time is 12:09"
s3 = "If 23:46 is the due date, then where is it?"
s4 = "#var#log#dogbite.1"
#!/usr/bin/env python3

import re
import fileinput


def main():
    line_number = 0

    for line in fileinput.input():
        line = line.rstrip()
        line_number += 1

        m = re.search(r" installed ((.+):(.+)) .*", line)
        if m:
            print("%d: %s" % (line_number, m.group(2)))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re
import fileinput


def main():
    line_number = 0

    pattern = re.compile(r" installed ((.+):(.+)) .*")

    for line in fileinput.input():
        line = line.rstrip()
        line_number += 1

        m = pattern.search(line)
        if m:
            print("%d: %s" % (line_number, m.group(2)))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re
import fileinput


def main():
    line_number = 0

    for line in fileinput.input():
        line = line.rstrip()
        line_number += 1

        m = re.search(r" installed (.+) .*", line)
        if m:
            print("%d: %s" % (line_number, m.group(1)))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re
import fileinput


def main():
    line_number = 0

    for line in fileinput.input():
        line = line.rstrip()
        line_number += 1

        m = re.search(r"installed (.+) .*", line)
        if m:
            print("%d: %s" % (line_number, m.group(1)))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re


def main():

    info = [("F", "Faraday Constant", 96485.332, "England"),
        ("c", "speed of light", 299792458, "Denmark"),
        ("h", "Planck Constant", 6.626e-34, "Germany"),
        ("m_e", "electron mass", 9.109e-31, "Great Britain")]

    text = """The ==NAME== (symbol '==SYMBOL==') has the magnitude ==VALUE==.
This was determined first in ==COUNTRY==.
"""

    for (symbol, name, number, place) in info:
        final = re.sub(r"==NAME==", name, text)
        final = re.sub(r"==SYMBOL==", symbol, final)
        final = re.sub(r"==COUNTRY==", place, final)
        final = re.sub(r"==VALUE==", "%.5E" % number, final)

        print(final)
        

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    date_from = sys.argv[1]
    date_to   = sys.argv[2] 

    # TODO: Complete your code here as described at the end of video # 2 for Lab 10.

    
    pattern = re.compile(r"(\d\d\d\d-\d\d-\d\d)( .+) installed (.+):(.*)")

    for line in sys.stdin:
        line = line.rstrip()

        m = pattern.search(line)
        if m:
            a = str(m.group(1))
            b = str(m.group(3))
            if date_from <= a <= date_to:
                print("%s: %s" % (a,b))


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import re
import sys

def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    inp = sys.argv[1]

    pattern = re.compile(r"(\d\d\d\d-\d\d-\d\d)( .+) installed (.+):(.*)")

    for line in sys.stdin:
        line = line.rstrip()

        m = pattern.search(line)
        if m:
            a = str(m.group(1))
            b = str(m.group(3))
            if a == inp:
                print("%s: %s" % (a,b))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

# usage: ./gen-message.py <csv-file-name>
import re
import datetime
import fileinput


template = """Nuttin'
Honey
"""

dirpath = "messages/"


def main():
    today = datetime.date.today()
    six_weeks_from_today = today + datetime.timedelta(weeks=6)

    today = today.strftime("%B %d %Y")
    six_weeks_from_today = six_weeks_from_today.strftime("%B %d %Y")

    for line in fileinput.input():
        pass


if __name__ == "__main__":
    main()
