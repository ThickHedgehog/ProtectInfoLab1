from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sqlite3
import enterWindow


class Ui_ChangePasswordWindow(QMainWindow):
    def __init__(self, Login):
        super(Ui_ChangePasswordWindow, self).__init__()

        self.EnterW = enterWindow.Ui_EnterWindow()
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
        self.Conf_Button.setGeometry(QtCore.QRect(330, 220, 150, 40))
        self.Conf_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Conf_Button.setMouseTracking(True)
        self.Conf_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Conf_Button.setObjectName("Conf_Button")

        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(330, 280, 150, 40))
        self.Exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Button.setMouseTracking(True)
        self.Exit_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Exit_Button.setObjectName("Exit_Button")

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setGeometry(QtCore.QRect(255, 100, 300, 40))
        self.Password.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                    "background-color: rgb(240, 217, 185);")
        self.Password.setObjectName("Password")

        self.Password_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_2.setGeometry(QtCore.QRect(255, 160, 300, 40))
        self.Password_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                      "background-color: rgb(240, 217, 185);")
        self.Password_2.setObjectName("Password_2")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.firstEnter(Login)
        self.addFunctionsClick(Login)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Conf_Button.setText(_translate("MainWindow", "Подтвердить"))
        self.Exit_Button.setText(_translate("MainWindow", "Выход"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Новый пароль"))
        self.Password_2.setPlaceholderText(_translate("MainWindow", "Повторите пароль"))
        self.label.setText(_translate("MainWindow", "Смена пароля"))

    def addFunctionsClick(self, Login):
        self.Conf_Button.clicked.connect(lambda: self.change(Login, self.Password.text(), self.Password_2.text()))
        self.Exit_Button.clicked.connect(lambda: self.exit())

    def firstEnter(self, Login):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        if Login != "":
            cur.execute("SELECT Password FROM Users WHERE Login = ?", (Login,))
            PasswordDB = cur.fetchall()
            if PasswordDB[0][0] == "":
                self.Conf_Button.setText("Установить")
                self.Exit_Button.hide()

    def change(self, Login, Password, PasswordConf):
        if Password == PasswordConf:
            db = sqlite3.connect("database.db")
            cur = db.cursor()
            cur.execute("SELECT Password FROM Users WHERE Login = ?", (Login,))
            PasswordDB = cur.fetchall()
            cur.execute("UPDATE Users SET Password = ? WHERE Login = ?", (Password, Login))
            db.commit()
            cur.close()
            db.close()
            self.Password.setText("")
            self.Password_2.setText("")
            if PasswordDB[0][0] == "":
                self.EnterW.show()
                self.close()

    def exit(self):
        self.EnterW.show()
        self.close()
