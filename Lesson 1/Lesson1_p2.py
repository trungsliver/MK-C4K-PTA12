from Lesson1_p1 import Human, Rectangle

# Khởi tạo đối tượng
human1 = Human('Hải meme', 15, 'male')

# Sử dụng phương thức __str__
print(human1)

# Sử dụng phương thức display_info
human1.display_info()

# Sử dụng phương thức say_hello
human1.say_hello()

# Sử dụng phương thức change_gender
human1.change_gender('meow')

# ======== BÀI TẬP ========
# Khởi tạo 1 HCN
hcn1 = Rectangle(5,2)

# Sử dụng phương thức tính chu vi
print('Chu vi HCN:', hcn1.chuvi())

# Sử dụng phương thức tính diện tích
print('Diện tích HCN:', hcn1.dien_tich())
