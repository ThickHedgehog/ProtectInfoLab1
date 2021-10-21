from PyQt5 import QtWidgets
import sys
import os
import decryptWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = decryptWindow.Ui_DecryptWindow()
    ui.show()
    ret = app.exec_()
    if ret == 0:
        os.remove("usersDataDecrypted.txt")
        sys.exit(ret)
