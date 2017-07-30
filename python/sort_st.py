#!/usr/bin/env python3

import operator
from operator import itemgetter, attrgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('chark', 'D', 30)
]


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

print(sorted(student_tuples, key=lambda student: student[2]))

print(sorted(student_tuples, key=itemgetter(1, 2)))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'C', 12),
    Student('hari', 'B', 12),
    Student('dave', 'B', 10),
    Student('apple', 'D', 20),
]

# sorted(student_objects, key=lambda student: student.age)   # sort by age

s1 = sorted(student_objects, key=lambda student: student.age)   # sort by age
print(s1)
s2 = sorted(student_objects, key=attrgetter('age'))
print(s2)
print(sorted(s2, key=attrgetter('name'), reverse=True))


l1 = [1, 2, 3]
l2 = [4, 5, 6]


operator.iconcat(l1, l2)
print(l1)
print(l2)
