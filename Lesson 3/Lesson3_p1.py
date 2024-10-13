class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.name} is {self.age} years old and is in {self.grade}"
    
    def lenLop(self):
        self.grade = self.grade + 1

    def change_name(self, new_name):
        self.name = new_name


