class Man:
    """
    Class fo description a human
    """

    def __init__(self, name, surname, ege):
        if not (name.isalpha() and surname.isalpha()):
            raise ValueError('Use only letters')
        if not ege.isdigit():
            raise ValueError('Use only numbers')
        self.name = name.title()
        self.surname = surname.title()
        self.ege = ege
    def __str__(self):
        return f'{self.name} {self.surname}\nEge-{self.ege}'
