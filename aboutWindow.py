from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_AboutWindow(QMainWindow):
    def __init__(self):
        super(Ui_AboutWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(500, 180)
        self.setStyleSheet("background-color: rgb(84, 42, 0);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 0, 470, 150))
        self.textBrowser.setStyleSheet("color: rgb(255, 179, 134);\n"
                                       "font: 75 18pt \"Times New Roman\";"
                                       "border-style: solid; border-width: 0px; border-color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Лабораторная №1"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\'; "
                                            "font-size:18pt; font-weight:72; font-style:normal;\">\n "
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Свицов "
                                            "Ростислав Олегович ИДБ-18-03</p>\n "
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Индивидуальное "
                                            "задание №21:</p>\n "
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Чередование "
                                            "букв, знаков препинания и снова букв.</p></body></html>"))
