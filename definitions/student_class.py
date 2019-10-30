"""
Program: student_class.py
Author: Colten pfander
Date last modified: 10/29/19


The purpose of this program is to make a unittest that tests the student_class for constructors, exception handling, and
validation.
"""


class Student:
    """Student class"""
    def __init__(self, l_name, f_name, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(l_name) and name_characters.issuperset(f_name) and name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float) and 0.0 <= float(gpa) <= 4.0:
            raise ValueError
        self.last_name = l_name
        self.first_name = f_name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
