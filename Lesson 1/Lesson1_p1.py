class Human:
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        # name, age, gender gọi là THUỘC TÍNH
        self.name = name
        self.age = age
        self.gender = gender
    
    # Phương thức __str__ dùng để print
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
    # Phương thức hiển thị thông tin
    def display_info(self):
        print(f'{self.name} - {self.age} tuổi - {self.gender}')

    # Phương thức chào hỏi
    def say_hello(self):
        print(f'Xin chào, tôi là {self.name}')

    # Phương thức chỉnh sửa thông tin
    def change_gender(self, new_gender):
        self.gender = new_gender    # gán giá trị mới cho gender
        self.display_info()         # hiện thông tin sau khi sửa

# ======== BÀI TẬP ========
class Rectangle:
    # Khởi tạo với 2 thuộc tính: a - chiều dài, b - chiều rộng
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # Phương thức tính chu vi HCN
    def chuvi(self):
        return 2*(self.a + self.b)
    # Phương thức tính diện tích HCN
    def dien_tich(self):
        return self.a * self.b
