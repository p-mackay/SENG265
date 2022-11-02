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
