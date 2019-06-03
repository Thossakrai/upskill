import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from controller.Organiser.OrgUpdateProfile import OrgImproveProfile
from screen.LrnProfile import Ui_Form


class LrnProfile(QWidget):
    def __init__(self, LearnerViewEnrolledCourseWindow, learner):
        QWidget.__init__(self, None)
        self.viewenrolledWindow = LearnerViewEnrolledCourseWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Go_back.clicked.connect(self.goback)
        self.ui.EditProf.clicked.connect(self.editdetail)
        self.learner = learner
        self.getProfile()

    def goback(self):
        self.hide()
        self.viewenrolledWindow.show()

    def editdetail(self):
        self.hide()
        self.EditProf = OrgImproveProfile(self, self.learner)
        self.EditProf.show()

    def getProfile(self):
        self.user_info = self.learner.getUserInfo()
        firstname = self.user_info.record(0).value("FNAME")
        lastname = self.user_info.record(0).value("LNAME")
        # birthdate = self.user_info.record(0).value("BIRTHDATE")
        username = self.user_info.record(0).value("USERNAME")
        phone = self.user_info.record(0).value("PHONE")
        mail = self.user_info.record(0).value("EMAIL")
        utype = self.user_info.record(0).value("UTYPE")
        upref = self.user_info.record(0).value("UPREF")
        gender = self.user_info.record(0).value("GENDER")
        self.ui.Lname.setText(lastname)
        self.ui.Fname.setText(firstname)
        self.ui.Sex.setText(gender)
        self.ui.Email.setText(mail)
        self.ui.Phone.setText(phone)
        self.ui.Type.setText(utype)
        self.ui.Pref.setText(upref)
        self.ui.Uname.setText(username)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnProfile()
    w.show()
    sys.exit(app.exec_())
