import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import login, signup

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = signup.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Sự kiên ấn nút signup => chuyển sang trang login
    ui.pushButton_signup.clicked.connect(login_w)
    MainWindow.show()

# Hiển thị trang login
def login_w():
    global ui
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Sự kiên ấn nút login => chuyển sang trang signup
    ui.pushButton_login.clicked.connect(homeUi)
    MainWindow.show()
#Run app
homeUi()
sys.exit(app.exec())

# Câu lệnh convert: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert: pyuic6 -x login.ui -o login.py