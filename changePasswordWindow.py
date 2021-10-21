from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import crypt
import binascii
import sqlite3

import adminWindow
import userWindow


class Ui_ChangePasswordWindow(QMainWindow):
    def __init__(self, Login, key, iv, hashPassword):
        super(Ui_ChangePasswordWindow, self).__init__()

        self.setObjectName("MainWindow")
        self.setFixedSize(800, 600)
        self.setWindowTitle("Лабараторная №1")
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(335, 50)
        self.label.setStyleSheet("font: 75 18pt \"Times New Roman\";\n"
                                 "color: rgb(255, 179, 134);")
        self.label.setObjectName("label")
        self.label.setFixedWidth(200)

        self.Conf_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Conf_Button.setGeometry(QtCore.QRect(330, 280, 150, 40))
        self.Conf_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Conf_Button.setMouseTracking(True)
        self.Conf_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Conf_Button.setObjectName("Conf_Button")

        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(330, 340, 150, 40))
        self.Exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Button.setMouseTracking(True)
        self.Exit_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Exit_Button.setObjectName("Exit_Button")

        self.Old_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Old_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Old_Password.setGeometry(QtCore.QRect(255, 100, 300, 40))
        self.Old_Password.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                        "background-color: rgb(240, 217, 185);")
        self.Old_Password.setObjectName("Password")

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

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.addFunctionsClick(Login, key, iv, hashPassword)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Conf_Button.setText(_translate("MainWindow", "Подтвердить"))
        self.Exit_Button.setText(_translate("MainWindow", "Выход"))
        self.Old_Password.setPlaceholderText(_translate("MainWindow", "Старый пароль"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Новый пароль"))
        self.Password_2.setPlaceholderText(_translate("MainWindow", "Повторите пароль"))
        self.label.setText(_translate("MainWindow", "Смена пароля"))

    def addFunctionsClick(self, Login, key, iv, hashPassword):
        self.Conf_Button.clicked.connect(
            lambda: self.change(Login, self.Old_Password.text(), self.Password.text(), self.Password_2.text(), key, iv,
                                hashPassword))
        self.Exit_Button.clicked.connect(lambda: self.exit(Login, key, iv, hashPassword))

    def change(self, Login, OldPassword, Password, PasswordConf, key, iv, hashPassword):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("SELECT Password FROM Users WHERE Login = ?", (Login,))
        PasswordDB = cur.fetchall()
        if Password == PasswordConf and PasswordDB[0][0] == OldPassword:
            cur.execute("SELECT Password FROM Users WHERE Login = ?", (Login,))
            PasswordDB = cur.fetchall()
            cur.execute("UPDATE Users SET Password = ? WHERE Login = ?", (Password, Login))
            db.commit()
            cur.close()
            db.close()
            self.Old_Password.setText("")
            self.Password.setText("")
            self.Password_2.setText("")
            if PasswordDB[0][0] == "":
                UserW = userWindow.Ui_UserWindow(Login, key, iv, hashPassword)
                UserW.show()
                self.close()

        self.fromDBtoTXT(key, iv)

    def exit(self, Login, key, iv, hashPassword):
        if Login == "ADMIN":
            AdminW = adminWindow.Ui_AdminWindow(key, iv, hashPassword)
            AdminW.show()
        else:
            UserW = userWindow.Ui_UserWindow(Login, key, iv, hashPassword)
            UserW.show()
        self.close()

    @staticmethod
    def fromDBtoTXT(key, iv):
        db = sqlite3.connect("database.db")

        cur = db.cursor()

        cur.execute("SELECT * FROM Users")
        data = cur.fetchall()

        cur.close()
        db.close()

        dataStr = ""

        for index in data:
            dataStr += str(index) + '\n'

        encrypted = crypt.encrypt(dataStr, key, iv)

        with open("usersData.txt", "w+") as f:
            hexEncrypted = binascii.hexlify(encrypted)
            f.write(str(hexEncrypted)[2:-1])

        with open("usersData.txt", "r") as f:
            text = f.read()
        text = bytes(text, 'ascii')
        text = binascii.unhexlify(text)

        decrypted = crypt.decrypt(text, key, iv)

        with open("usersDataDecrypted.txt", "w+") as f:
            f.write(str(decrypted.decode('ascii')))
