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

