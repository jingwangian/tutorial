#!/usr/bin/env python3


import sys
import datetime
import urllib.parse


class TaskResultQueueMsg():
    SUCCESS = 0
    FAILED = 1

    def __init__(self, task_id, task_result=SUCCESS):
        self.task_id = task_id
        self.task_result = task_result

class Person():
    name = ''
    age = 0
    addr = ''

    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr


class Student(Person):
    def __init__(self, name, age, addr, school, stu_class):
        self.school = school
        self.stu_class = stu_class
        super().__init__(name, age, addr)

    def __str__(self):
        # return '{self.name}--{self.age}--{self.addr}--{self.school}'.
        return '{}--{}--{}--{}--{}'.format(self.name, self.age, self.addr, self.school, self.stu_class)


class SchoolClass():
    student_list = []

    def __init__(self):
        self.student_numbers = 0


stu_a = Student('Jack', 12, 'city 01', 'city primary school', 'class 1')
stu_b = Student('John', 12, 'city 02', 'city primary school', 'class 1')
stu_c = Student('Jason', 13, 'city 03', 'city primary school', 'class 2')

print(stu_a)
print(stu_b)

print(dir(stu_a))
