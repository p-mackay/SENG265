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




