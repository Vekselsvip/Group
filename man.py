class Man:
    def __init__(self, name, surname, ege):
        self.name = name
        self.surname = surname
        self.ege = ege
    def __str__(self):
        return f'{self.name} {self.surname}\nEge-{self.ege}'


man_1 = Man('Petr1', 'Petrov1', 20)
man_2 = Man('Petr2', 'Petrov2', 19)
man_3 = Man('Petr3', 'Petrov3', 21)
man_4 = Man('Petr4', 'Petrov4', 20)
man_5 = Man('Petr5', 'Petrov5', 19)

