class Student_Info:
    def __init__(self, ids, name, tel, address, is_grade = False):
        self.ids = ids
        self.name = name
        self.tel = tel
        self.address = address
        self.is_grade = is_grade

    def __str__(self):
        return f'{self.ids}, {self.name}, {self.tel}, {self.address}, {self.is_grade}'