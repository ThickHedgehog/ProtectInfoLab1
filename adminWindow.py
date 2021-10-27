from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import enterWindow
import changePasswordWindow
import sqlite3
import crypt
import binascii


class Ui_AdminWindow(QMainWindow):
    def __init__(self, key, iv, hashPassword):
        super(Ui_AdminWindow, self).__init__()

        self.setObjectName("MainWindow")
        self.setFixedSize(800, 600)
        self.setWindowTitle("Лабараторная №1")
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.move(270, 50)
        self.label.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                 "color: rgb(255, 179, 134);")
        self.label.setObjectName("label")
        self.label.setFixedWidth(300)

        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(255, 100, 300, 40))
        self.Login.setStyleSheet("font: 14pt \"Times New Roman\";\n"
                                 "background-color: rgb(240, 217, 185);")
        self.Login.setObjectName("Login")

        self.Registration_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Registration_Button.setGeometry(QtCore.QRect(330, 160, 150, 40))
        self.Registration_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Registration_Button.setMouseTracking(True)
        self.Registration_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                               "background-color: rgb(162, 73, 0);")
        self.Registration_Button.setObjectName("Registration_Button")

        self.Change_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Button.setGeometry(QtCore.QRect(330, 220, 150, 40))
        self.Change_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Change_Button.setMouseTracking(True)
        self.Change_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                         "background-color: rgb(162, 73, 0);")
        self.Change_Button.setObjectName("Conf_Button")

        self.User = QtWidgets.QLabel(self.centralwidget)
        self.User.move(50, 390)
        self.User.setStyleSheet("font: 75 20pt \"Times New Roman\";\n"
                                "color: rgb(255, 179, 134);")
        self.User.setObjectName("User")
        self.User.setFixedWidth(500)

        self.Ban = QtWidgets.QCheckBox(self.centralwidget)
        self.Ban.move(300, 390)
        self.Ban.setStyleSheet("""QCheckBox::indicator {width: 40px; height: 40px;}""")

        self.Ban_Text = QtWidgets.QLabel(self.centralwidget)
        self.Ban_Text.move(340, 400)
        self.Ban_Text.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                    "color: rgb(255, 179, 134);")
        self.Ban_Text.setObjectName("Ban_Text")
        self.Ban_Text.setFixedWidth(120)

        self.Limit = QtWidgets.QCheckBox(self.centralwidget)
        self.Limit.move(500, 390)
        self.Limit.setStyleSheet("""QCheckBox::indicator {width: 40px; height: 40px;}""")

        self.Limit_Text = QtWidgets.QLabel(self.centralwidget)
        self.Limit_Text.move(540, 400)
        self.Limit_Text.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                      "color: rgb(255, 179, 134);")
        self.Limit_Text.setObjectName("Limit_Text")
        self.Limit_Text.setFixedWidth(250)

        self.Next_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_Button.setGeometry(QtCore.QRect(430, 430, 150, 40))
        self.Next_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Next_Button.setMouseTracking(True)
        self.Next_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Next_Button.setObjectName("Next_Button")

        self.Prev_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Prev_Button.setGeometry(QtCore.QRect(230, 430, 150, 40))
        self.Prev_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Prev_Button.setMouseTracking(True)
        self.Prev_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
                                       "background-color: rgb(162, 73, 0);")
        self.Prev_Button.setObjectName("Prev_Button")

        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(330, 540, 150, 40))
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

        self.firstUser()
        self.addFunctionsClick(key, iv, hashPassword)
        self.nowUserID = 1

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Панель администратора"))
        self.Login.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.Registration_Button.setText(_translate("MainWindow", "Создать"))
        self.Change_Button.setText(_translate("MainWindow", "Смена пароля"))
        self.Exit_Button.setText(_translate("MainWindow", "Выход"))
        self.Next_Button.setText(_translate("MainWindow", "Следующий"))
        self.Prev_Button.setText(_translate("MainWindow", "Предыдущий"))
        self.Ban_Text.setText(_translate("MainWindow", "Заблокировать"))
        self.Limit_Text.setText(_translate("MainWindow", "Установить ограничения"))

    def addFunctionsClick(self, key, iv, hashPassword):
        self.Registration_Button.clicked.connect(lambda: self.registration(self.Login.text(), key, iv))
        self.Change_Button.clicked.connect(lambda: self.change(key, iv, hashPassword))
        self.Next_Button.clicked.connect(lambda: self.nextUser())
        self.Prev_Button.clicked.connect(lambda: self.prevUser())
        self.Exit_Button.clicked.connect(lambda: self.exit(hashPassword))
        self.Ban.stateChanged.connect(lambda: self.ban(key, iv))
        self.Limit.stateChanged.connect(lambda: self.limit(key, iv))

    def registration(self, Login, key, iv):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users(ID INT, Login TEXT, Password TEXT, Banned INT, Limited INT)")
        cur.execute("SELECT Login FROM Users")
        LoginDB = str(cur.fetchall())
        cur.execute("SELECT ID FROM Users")
        ID = cur.fetchall()[::-1]
        banned = 0
        limited = 0
        if Login not in LoginDB and Login != "":
            cur.execute(f"INSERT INTO Users(ID, Login, Password, Banned, Limited) VALUES (?, ?, ?, ?, ?)",
                        (ID[0][0] + 1, Login, "", banned, limited))
            db.commit()
        cur.close()
        db.close()
        self.Login.setText("")

        self.fromDBtoTXT(key, iv)

    def change(self, key, iv, hashPassword):
        ChangeW = changePasswordWindow.Ui_ChangePasswordWindow("ADMIN", key, iv, hashPassword)
        ChangeW.show()
        self.close()

    def firstUser(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        cur.execute("SELECT Login FROM Users WHERE ID = ?", (1,))
        Login = cur.fetchall()

        cur.execute("SELECT Banned FROM Users WHERE ID = ?", (1,))
        banned = cur.fetchall()

        cur.execute("SELECT Limited FROM Users WHERE ID = ?", (1,))
        limited = cur.fetchall()

        cur.close()
        db.close()

        self.User.setText(Login[0][0])
        if banned[0][0] == 1:
            self.Ban.setChecked(True)
        else:
            self.Ban.setChecked(False)

        if limited[0][0] == 1:
            self.Limit.setChecked(True)
        else:
            self.Limit.setChecked(False)

    def ban(self, key, iv):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        if self.Ban.isChecked():
            cur.execute("UPDATE Users SET Banned = ? WHERE ID = ?", (1, self.nowUserID))
            db.commit()
        else:
            cur.execute("UPDATE Users SET Banned = ? WHERE ID = ?", (0, self.nowUserID))
            db.commit()

        if self.Limit.isChecked():
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (1, self.nowUserID))
            db.commit()
        else:
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (0, self.nowUserID))
            db.commit()

        cur.close()
        db.close()

        self.fromDBtoTXT(key, iv)

    def limit(self, key, iv):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        if self.Limit.isChecked():
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (1, self.nowUserID))
            db.commit()
        else:
            cur.execute("UPDATE Users SET Limited = ? WHERE ID = ?", (0, self.nowUserID))
            db.commit()

        cur.close()
        db.close()

        self.fromDBtoTXT(key, iv)

    def nextUser(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()
        cur.execute("SELECT ID FROM Users")
        ID = cur.fetchall()[::-1]

        if self.nowUserID + 1 <= ID[0][0]:
            cur.execute("SELECT Login FROM Users WHERE ID = ?", (self.nowUserID + 1,))
            Login = cur.fetchall()

            self.User.setText(Login[0][0])
            self.nowUserID += 1

            cur.execute("SELECT Banned FROM Users WHERE ID = ?", (self.nowUserID,))
            banned = cur.fetchall()

            cur.execute("SELECT Limited FROM Users WHERE ID = ?", (self.nowUserID,))
            limited = cur.fetchall()

            cur.close()
            db.close()

            if banned[0][0] == 1:
                self.Ban.setChecked(True)
            else:
                self.Ban.setChecked(False)

            if limited[0][0] == 1:
                self.Limit.setChecked(True)
            else:
                self.Limit.setChecked(False)

    def prevUser(self):
        db = sqlite3.connect("database.db")
        cur = db.cursor()

        if self.nowUserID - 1 > 0:
            cur.execute("SELECT Login FROM Users WHERE ID = ?", (self.nowUserID - 1,))
            Login = cur.fetchall()

            self.User.setText(Login[0][0])
            self.nowUserID -= 1

            cur.execute("SELECT Banned FROM Users WHERE ID = ?", (self.nowUserID,))
            banned = cur.fetchall()

            cur.execute("SELECT Limited FROM Users WHERE ID = ?", (self.nowUserID,))
            limited = cur.fetchall()

            cur.close()
            db.close()

            if banned[0][0] == 1:
                self.Ban.setChecked(True)
            else:
                self.Ban.setChecked(False)

            if limited[0][0] == 1:
                self.Limit.setChecked(True)
            else:
                self.Limit.setChecked(False)

    def exit(self, hashPassword):
        EnterW = enterWindow.Ui_EnterWindow(hashPassword)
        EnterW.show()
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
