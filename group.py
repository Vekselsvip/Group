from man import *
from student import *
from error import InputError


class Group:
    """
    module for add students in group.
    """
    def __init__(self, name):
        self.name = name
        self.students = []

    def __str__(self):
        st = []
        for i in self.students:
            st.append(i.surname)
        return f'Class - {self.name}\n{st}'

    def add_st(self, st):
        if not isinstance(st, Student):
            raise TypeError(f"'{st.surname}' not a Student")
        self.students.append(st)

    def del_st(self, st):
        if not isinstance(st, Student):
            raise TypeError(f"'{st.surname}' not a Student")
        self.students.remove(st)

    def st_info(self, surname):
        for i in self.students:
            if i.surname == surname:
                return i
