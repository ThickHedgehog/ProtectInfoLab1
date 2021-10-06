from PyQt5 import QtWidgets
import sys
import enterWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = enterWindow.Ui_EnterWindow()
    ui.show()
    sys.exit(app.exec_())
