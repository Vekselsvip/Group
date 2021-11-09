from man import *
from error import InputError


class Student(Man):
    count = 0
    """
    student creation
    """
    def __init__(self, name, surname, ege, course):
        if not isinstance(course, int):
            raise InputError(course, 'Write number for course')
        super().__init__(name, surname, ege)
        self.course = course

        Student.count += 1

    def __str__(self):
        return f"Student: {super().__str__()}\ncourse -  {self.course}"


st_1 = Student('Ivan', 'Ivanoov', '20', 2)
st_2 = Student('Petr', 'Ivanov', '20', 2)