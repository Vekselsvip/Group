from man import *
from error import InputError


class Student(Man):
    """
    student creation
    """
    def __init__(self, name, surname, ege, course):
        if not isinstance(course, int):
            raise InputError(course, 'Write number for course')
        super().__init__(name, surname, ege)
        self.course = course

    def __str__(self):
        return f"Student: {super().__str__()}\ncourse -  {self.course}"
