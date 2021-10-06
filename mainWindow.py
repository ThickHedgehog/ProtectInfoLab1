from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import enterWindow
import aboutWindow

import sqlite3


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.AboutW = aboutWindow.Ui_AboutWindow()
        self.EnterW = enterWindow.Ui_EnterWindow()
        self.setObjectName("MainWindow")
        self.setFixedSize(800, 600)
        self.setWindowTitle("Лабараторная №1")
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(340, 50)
        self.label.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
                                 "color: rgb(255, 179, 134);")
        self.label.setObjectName("label")
        self.label.setFixedWidth(200)

        self.Registration_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Registration_Button.setGeometry(QtCore.QRect(330, 280, 150, 40))
        self.Registration_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Registration_Button.setMouseTracking(True)
        self.Registration_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                               "background-color: rgb(162, 73, 0);")
        self.Registration_Button.setObjectName("Registration_Button")

        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(255, 100, 300, 40))
        self.Login.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                 "background-color: rgb(240, 217, 185);")
        self.Login.setObjectName("Login")

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setGeometry(QtCore.QRect(255, 160, 300, 40))
        self.Password.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                    "background-color: rgb(240, 217, 185);")
        self.Password.setObjectName("Password")

        self.Password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_2.setGeometry(QtCore.QRect(255, 220, 300, 40))
        self.Password_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                      "background-color: rgb(240, 217, 185);")
        self.Password_2.setObjectName("Password_2")

        self.Enter_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Enter_Button.setGeometry(QtCore.QRect(330, 340, 150, 40))
        self.Enter_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Enter_Button.setMouseTracking(True)
        self.Enter_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                        "background-color: rgb(162, 73, 0);")
        self.Enter_Button.setObjectName("Enter_Button")

        self.About_Button = QtWidgets.QPushButton(self.centralwidget)
        self.About_Button.setGeometry(QtCore.QRect(630, 540, 150, 40))
        self.About_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.About_Button.setMouseTracking(True)
        self.About_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                        "background-color: rgb(162, 73, 0);")
        self.About_Button.setObjectName("Enter_Button")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.addFunctionsClick()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Registration_Button.setText(_translate("MainWindow", "Регистрация"))
        self.Login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.Password_2.setPlaceholderText(_translate("MainWindow", "Повторите пароль"))
        self.Enter_Button.setText(_translate("MainWindow", "Вход"))
        self.About_Button.setText(_translate("MainWindow", "О программе"))
        self.label.setText(_translate("MainWindow", "Регистрация"))

    def addFunctionsClick(self):
        self.Registration_Button.clicked.connect(lambda: self.registration(self.Login.text(), self.Password.text(),
                                                                           self.Password_2.text()))
        self.Enter_Button.clicked.connect(lambda: self.enter())
        self.About_Button.clicked.connect(lambda: self.about())

    def registration(self, Login, Password, PasswordConf):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users(ID INT, Login TEXT, Password TEXT, Banned INT, Limited INT)")
        cur.execute("SELECT Login FROM Users")
        LoginDB = str(cur.fetchall())
        cur.execute("SELECT ID FROM Users")
        ID = cur.fetchall()[::-1]
        banned = 0
        limited = 0
        if Login not in LoginDB and Login != "" and Password != "" and Password == PasswordConf:
            cur.execute(f"INSERT INTO Users(ID, Login, Password, Banned, Limited) VALUES (?, ?, ?, ?, ?)",
                        (ID[0][0] + 1, Login, Password, banned, limited))
            db.commit()
        cur.close()
        db.close()
        self.Login.setText("")
        self.Password.setText("")
        self.Password_2.setText("")

    def enter(self):
        self.EnterW.show()
        self.close()

    def about(self):
        self.AboutW.show()
