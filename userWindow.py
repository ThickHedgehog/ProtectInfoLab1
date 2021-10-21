from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import enterWindow
import sqlite3
import changePasswordWindow


class Ui_UserWindow(QMainWindow):
    def __init__(self, Login, key, iv, hashPassword):
        super(Ui_UserWindow, self).__init__()

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

        self.Change_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Button.setGeometry(QtCore.QRect(330, 100, 150, 40))
        self.Change_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Change_Button.setMouseTracking(True)
        self.Change_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                         "background-color: rgb(162, 73, 0);")
        self.Change_Button.setObjectName("Conf_Button")

        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(330, 160, 150, 40))
        self.Exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Button.setMouseTracking(True)
        self.Exit_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Exit_Button.setObjectName("Exit_Button")

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.firstEnter(Login, key, iv, hashPassword)
        self.addFunctionsClick(Login, key, iv, hashPassword)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Change_Button.setText(_translate("MainWindow", "Смена пароля"))
        self.Exit_Button.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Аккаунт"))

    def addFunctionsClick(self, Login, key, iv, hashPassword):
        self.Exit_Button.clicked.connect(lambda: self.exit(hashPassword))
        self.Change_Button.clicked.connect(lambda: self.change(Login, key, iv, hashPassword))

    def firstEnter(self, Login, key, iv, hashPassword):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("SELECT Password FROM Users WHERE Login = ?", (Login,))
        PasswordDB = cur.fetchall()
        cur.execute("SELECT Limited FROM Users WHERE Login = ?", (Login,))
        Limited = cur.fetchall()
        cur.execute("SELECT Banned FROM Users WHERE Login = ?", (Login,))
        Banned = cur.fetchall()
        if PasswordDB[0][0] == "" or Limited[0][0] and Banned[0][0] == 0:
            ChangeW = changePasswordWindow.Ui_ChangePasswordWindow(Login, key, iv, hashPassword)
            ChangeW.Conf_Button.setText("Установить")
            ChangeW.Exit_Button.hide()
            ChangeW.Old_Password.hide()
            ChangeW.show()
            self.close()
        cur.close()
        db.close()

    def change(self, Login, key, iv, hashPassword):
        ChangeW = changePasswordWindow.Ui_ChangePasswordWindow(Login, key, iv, hashPassword)
        ChangeW.show()
        self.close()

    def exit(self, hashPassword):
        EnterW = enterWindow.Ui_EnterWindow(hashPassword)
        EnterW.show()
        self.close()
