import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import login, signup

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

users = ['admin:admin']

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Sự kiên ấn nút signup => chuyển sang trang login
    ui.pushButton_signup.clicked.connect(signup_check)
    MainWindow.show()

# Hàm kiểm tra đăng ký
def signup_check():
    check = True
    # Lấy thông tin từ giao diện
    name = ui.lineEdit_name.text().strip()
    email = ui.lineEdit_email.text().strip()
    password = ui.lineEdit_password.text().strip()
    confirm = ui.lineEdit_confirm.text().strip()

    # Kiểm tra thiếu thông tin
    if name == '' or email == '' or password == '' or confirm == '':
        check = False
        msg_box('Signup fail', 'Missing information!')
    # Kiểm tra passwword và confirm không khớp
    elif password != confirm:
        check = False
        msg_box('Signup fail', 'Password and confirm password not match!')
    # Kiểm tra email đã tồn tại:
    else:
        for user in users:
            stored_email, stored_passwword = user.split(':', 1)
            if email == stored_email:
                check = False
                msg_box('Signup fail', 'Email already exists!')
    
    # Kiểm tra xem có đăng ký thành công không
    if check == True:
        # Thêm tài khoản mới vào danh sách users
        users.append(f'{email}:{password}')
        msg_box('Signup success', 'Signup success!')
        print(users)
        # Chuyển sang trang login
        login_w()
    else:
        ui.lineEdit_name = ''
        ui.lineEdit_email = ''
        ui.lineEdit_password = ''
        ui.lineEdit_confirm = ''

# Hiển thị trang login
def login_w():
    global ui
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Sự kiên ấn nút login => chuyển sang trang signup
    ui.pushButton_login.clicked.connect(login_check)
    MainWindow.show()

# Kiểm tra đăng nhập
def login_check():
    check = False
    username = ui.lineEdit_username.text().strip()
    password = ui.lineEdit_password.text().strip()
    # Kiểm tra 
    for user in users:
        stored_username, stored_password = user.split(':', 1)
        if username == stored_username and password == stored_password:
            check = True
    
    if check == True:
        msg_box('Login success', 'Welcome to my app !!!')
        homeUi()
    else:
        msg_box('Login fail', 'Username or password is incorrect!')


# Hộp thoại thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

#Run app
homeUi()
sys.exit(app.exec())

# Câu lệnh convert: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert: pyuic6 -x login.ui -o login.py