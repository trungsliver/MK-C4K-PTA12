# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal ExtraBold")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 360, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 420, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 300, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(200, 120, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal Medium")
        font.setPointSize(10)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("padding-left: 5px;")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_confirm = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_confirm.setGeometry(QtCore.QRect(200, 420, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal Medium")
        font.setPointSize(10)
        self.lineEdit_confirm.setFont(font)
        self.lineEdit_confirm.setStyleSheet("padding-left: 5px;")
        self.lineEdit_confirm.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(200, 360, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal Medium")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet("padding-left: 5px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(200, 180, 400, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal Medium")
        font.setPointSize(10)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("padding-left: 5px;")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(300, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(420, 240, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(200, 300, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal Medium")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(100, 480, 331, 18))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal Medium")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("padding-left: 5px;")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_signup = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_signup.setGeometry(QtCore.QRect(325, 520, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Nunito Sans Normal ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 85, 0);\n"
"    color: white;\n"
"    border: 2px solid rgb(255, 85, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top: 3px;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 85, 0, 0.8);\n"
"    color: white;\n"
"}")
        self.pushButton_signup.setObjectName("pushButton_signup")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SIGN UP"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "Gender:"))
        self.label_5.setText(_translate("MainWindow", "Confirm:"))
        self.label_6.setText(_translate("MainWindow", "Email:"))
        self.label_7.setText(_translate("MainWindow", "DOB:"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "Input your name"))
        self.lineEdit_confirm.setPlaceholderText(_translate("MainWindow", "Confirm your password"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Input your email"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.radioButton_3.setText(_translate("MainWindow", "Others"))
        self.checkBox.setText(_translate("MainWindow", "I Agree to the Terms and Conditions"))
        self.pushButton_signup.setText(_translate("MainWindow", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
