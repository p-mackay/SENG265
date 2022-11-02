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
