import sys

from DeleteCourse import OrgDelete
from OrganiserViewACourse import OrgViewAll
from CreateCourses import OrgCreate
from Org_ViewProfile import OrgProfile
from screen.OrgMenu import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class LearnerMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.profile.clicked.connect(self.Profile)
        self.ui.create.clicked.connect(self.CreateCourse)
        self.ui.display.clicked.connect(self.OrgViewAll)
        self.ui.delete_2.clicked.connect(self.OrgDel)



    def Profile(self):
        self.hide()
        self.prof = OrgProfile(self)
        self.prof.show()

    def CreateCourse(self):
        self.hide()
        self.create = OrgCreate(self)
        self.create.show()

    def OrgViewAll(self):
        self.hide()
        self.viewall = OrgViewAll(self)
        self.viewall.show()

    def OrgDel(self):
        self.hide()
        self.eliminate = OrgDelete(self, self.uname)
        self.eliminate.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LearnerMenu()
    w.show()
    sys.exit(app.exec_())