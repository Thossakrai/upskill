import sys

from screen.orgreg import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class Register(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self, None)
        self.mainWindow = mainWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Signup_2.clicked.connect(self.GoBack)

    def GoBack(self):
        self.hide()
        self.mainWindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Register()
    w.show()
    sys.exit(app.exec_())
