import sys
from PyQt6 import QtGui, QtWidgets, QtCore
import lesson8, image_rc

# QApplication: quản lý phần giao diện ứng dụng
# QMainWindow: tạo cửa sổ ứng dụng chính

#xu ly
ui = ''
app = QtWidgets.QApplication(sys.argv) 
MainWindow = QtWidgets.QMainWindow()

def homeUi():
    global ui
    ui = lesson8.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

#Run app
homeUi()
sys.exit(app.exec())

# Câu lệnh convert: pyuic6 -x signup.ui -o signup.py
# Câu lệnh convert: pyuic6 -x lesson8.ui -o lesson8.py
# Câu lệnh convert qrc: pyside6-rcc image.qrc -o image_rc.py
