import sys

from LearnerMenu import LearnerMenu
from Register import Register
from screen.signin import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class SignInUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.BeLrn)
        self.ui.pushButton_3.clicked.connect(self.BeOrg)
        self.ui.pushButton.clicked.connect(self.Login)

    def Login(self):
        self.hide()
        self.LrnMenu = LearnerMenu(self)
        self.LrnMenu.show()


    def BeOrg(self):
        self.hide()
        self.Register = Register(self)
        self.Register.show()

    def BeLrn(self):
        self.hide()
        self.Register = Register(self)
        self.Register.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SignInUI()
    w.show()
    sys.exit(app.exec_())
    