import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from screen.OrgUpdateProf import Ui_Form
from backend.User import *


class OrgImproveProfile(QWidget):
    def __init__(self, OrganiserMenuWindow, learner):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.ui.save.clicked.connect(self.updateinfo)
        self.learner = learner
        self.getInfo()

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def updateinfo(self):
        self.hide()
        self.orgmenuWindow.show()

    def getInfo(self):
        self.profile = Organiser("tsk")
        self.user_profile = self.profile.getUserInfo()
        fname = self.user_profile.record(0).value("FNAME")
        lname = self.user_profile.record(0).value("LNAME")
        bd = self.user_profile.record(0).value("BIRTHDATE")
        phone = self.user_profile.record(0).value("PHONE")
        email = self.user_profile.record(0).value("EMAIL")
        utype = self.user_profile.record(0).value("UTYPE")
        upref = self.user_profile.record(0).value("UPREF")
        gender = self.user_profile.record(0).value("GENDER")
        self.ui.Lname.setText(lname)
        self.ui.Fname.setText(fname)
        self.ui.Sex.setCurrentText(gender)
        self.ui.User.setText(self.learner.uname)
        self.ui.email.setText(email)
        self.ui.phone.setText(phone)
        self.ui.type.setCurrentText(upref)


        # self.ui.User.setText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgImproveProfile()
    w.show()
    sys.exit(app.exec_())
