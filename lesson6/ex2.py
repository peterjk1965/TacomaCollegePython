#!/usr/bin/python3


class Time:
    """ Blueprint for a Time object"""
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
          print (self.__hour, ":", self.__minute, ":", self.__second)

    def set_second(self, second):
       self.__second = second

    def get_second(self):
       return self.__second