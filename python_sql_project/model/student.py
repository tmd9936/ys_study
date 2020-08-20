class Student:
    def __init__(self, ids, os_grade, cv_grade, db_grade):
        self.ids = ids
        self.os_grade = os_grade
        self.cv_grade = cv_grade
        self.db_grade = db_grade

    def __str__(self):
        return f'{self.ids}, {self.os_grade}, {self.cv_grade}, {self.db_grade}'
        
        