from Lesson2_p1 import Human, Student, VatNuoi
from Lesson2_p1 import Xe, XeHoi, XeDap

stu1 = Student('Bảo Nam', 12, 'Lớp 7')
print(stu1)
stu1.xin_chao()

animal1 = VatNuoi('Loopy', 'Pink', 5, '20kg')
print(animal1)
animal1.thong_tin()

xe1 = Xe('Honda', 'black', '50M')
xe2 = XeHoi('BMW', 'Grey', '3B')
xe3 = XeDap('Road', 'Red', '5M')

xe1.khoi_dong()
xe2.chay_bang_bon_banh()
xe3.dap_bang_hai_chan()