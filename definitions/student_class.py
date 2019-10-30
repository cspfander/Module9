"""
Program: student_class.py
Author: Colten pfander
Date last modified: 10/29/19


The purpose of this program is to make a unittest that tests the student_class for constructors, exception handling, and
validation.
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)