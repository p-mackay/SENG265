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
