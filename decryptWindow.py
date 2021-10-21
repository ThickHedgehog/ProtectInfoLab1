from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import enterWindow
import errorWindow


class Ui_DecryptWindow(QMainWindow):
    def __init__(self):
        super(Ui_DecryptWindow, self).__init__()

        self.password = "1234"

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

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.addFunctionsClick()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Password.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.Enter_Button.setText(_translate("MainWindow", "Вход"))
        self.label.setText(_translate("MainWindow", "Расшифровка"))

    def addFunctionsClick(self):
        self.Enter_Button.clicked.connect(lambda: self.enter(self.Password.text()))

    def enter(self, enterPassword):
        if enterPassword == self.password:
            enterW = enterWindow.Ui_EnterWindow(enterPassword)
            enterW.show()
            self.close()
        else:
            errorW = errorWindow.Ui_ErrorWindow()
            errorW.textBrowser.setText('<html><body><table><tr><td align = "center" width = '
                                       '"100%">Неверный пароль</td></tr></table></body></html>')
            errorW.show()
