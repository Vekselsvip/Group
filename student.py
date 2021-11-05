from man import *


class Student(Man):
    def __init__(self, name, surname, ege, course):
        super().__init__(name, surname, ege)
        self.course = course

    def __str__(self):
        return f"Student: {super().__str__()}\ncourse -  {self.course}"


st_1 = Student('Petr1', 'Petrov1', 20, 3)
st_2 = Student('Petr2', 'Petrov2', 19, 2)
st_3 = Student('Petr3', 'Petrov3', 21, 4)
st_4 = Student('Petr4', 'Petrov4', 20, 2)
st_5 = Student('Petr5', 'Petrov5', 19, 2)

