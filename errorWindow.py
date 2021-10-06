from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow


class Ui_ErrorWindow(QMainWindow):
    def __init__(self):
        super(Ui_ErrorWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(500, 280)
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 80, 500, 150))
        self.textBrowser.setStyleSheet("color: rgb(255, 179, 134);\n"
                                       "font: 75 18pt \"Times New Roman\";"
                                       "border-style: solid; border-width: 0px; border-color: black;")
        self.textBrowser.setObjectName("textBrowser")

        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(180, 220, 150, 40))
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

        self.addFunctionsClick()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Лабораторная №1"))
        self.Exit_Button.setText(_translate("MainWindow", "Ок"))

    def addFunctionsClick(self):
        self.Exit_Button.clicked.connect(lambda: self.exit())

    def exit(self):
        self.close()
