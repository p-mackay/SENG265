#!/usr/bin/env python3
class Person:
    def __init__(self, first, last, age):
        self.__first = first
        self.__last = last
        self.__age = age

    def printPerson(self):
        print(f"{self.__first}")
        print(f"{self.__last}")
        print(f"{self.__age}")

