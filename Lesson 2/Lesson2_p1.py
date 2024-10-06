class Human():
    def __init__(self, name, age):
        # name, age là thuộc tính
        self.name = name
        self.age = age
    # Phương thức __str__ để hiện data
    def __str__(self):
        return f'{self.name} - {self.age} tuổi'
    # Phương thức xin chào
    def xin_chao(self):
        print(f'{self.name} xin chào mọi người')

# Lớp Student kế thừa từ Human
class Student(Human):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# Bài tập
class VatNuoi():
    def __init__(self, Giong, MauSac, Tuoi, CanNang):
        self.Giong = Giong
        self.MauSac = MauSac
        self.Tuoi = Tuoi
        self.CanNang = CanNang
    def __str__(self):
        return f'{self.Giong} - {self.MauSac} - {self.Tuoi} - {self.CanNang}'
    def thong_tin(self):
        print(f'{self.Giong} - {self.MauSac} - {self.Tuoi} - {self.CanNang}')