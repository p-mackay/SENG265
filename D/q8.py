#!/usr/bin/env python3

import math

class Circle:
    '''Circle class'''
    __objCount: int = 100

    def __init(self, radius: float):
        Circle.__objCount+=1
        self.__radius = radius

    def get_obj_count() -> int:
        return Circle.__objCount

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return self.__radius * self.__radius * math.floor(math.pi)

def main() ->object:
    fs: str = f("Object no generated: ")
    c: Circle = Circle(3)
    objs: int = Circle.get_obj_count()
    area: int = c.get_area()
    print(f"Area = {area} "+fs+f'{objs}')

    for k in range(3):
        c = Circle(4)
        objs = Circle.get_obj_count()
        area = c.get_area()
        print(f'Area = {area} '+fs+f'{objs}')

if __name__ == "__main__":
    main()
