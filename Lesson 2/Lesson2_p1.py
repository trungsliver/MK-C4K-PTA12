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

class Xe:
    def __init__(self, hang, mau_sac, gia_tien):
        self.hang = hang
        self.mau_sac = mau_sac
        self.gia_tien = gia_tien
    def khoi_dong(self):
        print(f'Xe {self.hang} đang khởi động')

class XeHoi(Xe):
    def __init__(self, hang, mau_sac, gia_tien):
        super().__init__(hang, mau_sac, gia_tien)
    def chay_bang_bon_banh(self):
        print(f'Xe {self.hang} đang chạy về phía trước bằng động cơ')

class XeDap(Xe):
    def __init__(self, hang, mau_sac, gia_tien):
        super().__init__(hang, mau_sac, gia_tien)
    def dap_bang_hai_chan(self):
        print(f'Xe {self.hang} đang được đạp về phía trước')