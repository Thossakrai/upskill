import sys

from controller.LearnerMenu import LearnerMenu
from controller.Register import Register
from screen.signin import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from backend.loginsystem import *
from controller.OrganiserMenu import OrganiserMenu
from PySide2.QtMultimedia import QSound


class LoginUI(QWidget):
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
        self.loginsystem = LoginSystem(self.ui.lineEdit.text(), self.ui.lineEdit_2.text())
        utype = self.loginsystem.isValidUser()
        if utype[0] == 'LRN' :
            self.hide()
            self.LrnMenu = LearnerMenu(self, self.ui.lineEdit.text(), utype[1])
            self.LrnMenu.show()
        elif utype[0] == 'ORG' :
            self.hide()
            self.OrgMenu = OrganiserMenu(self, self.ui.lineEdit.text(), utype[1])
            self.OrgMenu.show()



    def BeOrg(self):
        self.hide()
        self.Register = Register(self, "ORG")
        self.Register.show()


    def BeLrn(self):
        self.hide()
        self.Register = Register(self, "LRN")
        self.Register.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LoginUI()
    w.show()
    sys.exit(app.exec_())
    