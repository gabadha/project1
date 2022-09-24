# Author: Fardoza Sheikh-Nur
# GitHub username: gabadha
# Date: 9/23/2022
# Description: This code calculates mean/median/mode stats of a list of give grades


import statistics
""" Importing the statistics module"""


class Student:
    """ Represents students with names and grades"""

    def __init__(self, student_name, student_grade):
        self._student_name = student_name
        self._student_grade = student_grade

    def get_grade(self):
        # Returns the grade
        return self._student_grade


def basic_stats():
    Student.get_grade = (95, 92, 98, 85)
    return statistics.mean(Student.get_grade), statistics.median(Student.get_grade), statistics.mode(Student.get_grade)
    # Returns a tuple containing mean, median and mode of all given grades


print(basic_stats())
