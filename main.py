import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from controller.Learner.LearnerMenu import LearnerMenu
from controller.Register import Register
from controller.Organiser.OrganiserMenu import OrganiserMenu
from screen.signin import Ui_Form
from backend.User import *


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
        uname = self.ui.lineEdit.text()
        pw = self.ui.lineEdit_2.text()
        self.user = User(uname, pw)
        utype = self.user.login()
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
    