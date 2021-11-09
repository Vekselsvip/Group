from man import *
from student import *
from error import InputError
from iter import *


class Group:
    count = 0
    """
    module for add students in group.
    """
    def __init__(self, name):
        self.name = name
        self.students = []

        Group.count += 1

    def __str__(self):
        st = []
        for i in self.students:
            st.append(i.surname)
        s = '\n'.join(map(str, st))
        return f'Class - {self.name}\n{s}'

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

    def __iter__(self):
        return GroupIterator(self.students)


group_1 = Group('It')
group_1.add_st(st_1)
group_1.add_st(st_2)

print(group_1)
