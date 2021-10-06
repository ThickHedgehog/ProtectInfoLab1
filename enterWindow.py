from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import mainWindow
import changePasswordWindow
import adminWindow
import aboutWindow
import errorWindow
import sqlite3


class Ui_EnterWindow(QMainWindow):
    def __init__(self):
        super(Ui_EnterWindow, self).__init__()

        self.i = 0

        self.AboutW = aboutWindow.Ui_AboutWindow()
        self.setObjectName("MainWindow")
        self.setFixedSize(800, 600)
        self.setWindowTitle("Лабараторная №1")
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(375, 50)
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
        self.Registration_Button.hide()

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

        self.Enter_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Enter_Button.setGeometry(QtCore.QRect(330, 220, 150, 40))
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
        self.Enter_Button.setText(_translate("MainWindow", "Вход"))
        self.label.setText(_translate("MainWindow", "Вход"))
        self.About_Button.setText(_translate("MainWindow", "О программе"))

    def addFunctionsClick(self):
        self.Registration_Button.clicked.connect(lambda: self.registration())
        self.Enter_Button.clicked.connect(lambda: self.enter(self.Login.text(), self.Password.text()))
        self.About_Button.clicked.connect(lambda: self.about())

    def registration(self):
        RegW = mainWindow.Ui_MainWindow()
        RegW.show()
        self.close()

    def enter(self, Login, Password):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        AdminW = adminWindow.Ui_AdminWindow()
        errorW = errorWindow.Ui_ErrorWindow()
        userFlag = False
        if Login != "":
            cur.execute("SELECT Login FROM Users")
            Users = cur.fetchall()
            for i in Users:
                if i[0] == Login:
                    userFlag = True
                    break
            if userFlag:
                ChangeW = changePasswordWindow.Ui_ChangePasswordWindow(Login)
                if self.i > 1:
                    self.close()
                else:
                    cur.execute("SELECT Password FROM Users WHERE Login = ?", (Login,))
                    PasswordDB = cur.fetchall()
                    if Login == "ADMIN" and Password == PasswordDB[0][0]:
                        AdminW.show()
                        self.close()
                    elif Password == PasswordDB[0][0]:
                        self.i = 0
                        cur.execute("SELECT Banned FROM Users WHERE Login = ?", (Login,))
                        banned = cur.fetchall()

                        cur.execute("SELECT Limited FROM Users WHERE Login = ?", (Login,))
                        limited = cur.fetchall()
                        if banned[0][0] == 1:
                            errorW.textBrowser.setText('<html><body><table><tr><td align = "center" width = '
                                                       '"100%">Вам бан!</td></tr></table></body></html>')
                            errorW.show()
                        else:
                            if limited[0][0] == 1:
                                if self.checkLimit(Password):
                                    ChangeW.show()
                                    self.close()
                                else:
                                    ChangeW.show()
                                    errorW.textBrowser.setText('<html><body><table><tr><td align = "center" width = '
                                                               '"100%">Пароль не соответствует '
                                                               'ограничениям</td></tr></table></body></html>')
                                    errorW.show()
                                    self.close()
                            else:
                                ChangeW.show()
                                self.close()
                    else:
                        errorW.textBrowser.setText('<html><body><table><tr><td align = "center" width = '
                                                   '"100%">Неверный пароль</td></tr></table></body></html>')
                        errorW.show()
                        self.i += 1
            else:
                errorW.textBrowser.setText('<html><body><table><tr><td align = "center" width = '
                                           '"100%">Неверный логин</td></tr></table></body></html>')
                errorW.show()
        else:
            errorW.textBrowser.setText('<html><body><table><tr><td align = "center" width = '
                                       '"100%">Пустой логин</td></tr></table></body></html>')
            errorW.show()

        cur.close()
        db.close()
        self.Login.setText("")
        self.Password.setText("")

    @staticmethod
    def checkLimit(Password):
        alf = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        dig = ",.?!;:"
        letter = True
        digit = False
        flag = True

        for i in Password:
            if letter is True and digit is False:
                if i in alf:
                    letter = False
                    digit = True
                    continue
                else:
                    flag = False
                    break

            if letter is False and digit is True:
                if i in dig:
                    letter = True
                    digit = False
                    continue
                else:
                    flag = False
                    break

        return flag

    def about(self):
        self.AboutW.show()
