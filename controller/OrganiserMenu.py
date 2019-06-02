import sys

from controller.DeleteCourse import OrgDelete
from controller.OrganiserViewACourse import OrgViewAll
from controller.CreateCourses import OrgCreate
from controller.Org_ViewProfile import OrgProfile
from screen.OrgMenu import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from PySide2.QtMultimedia import QSound


class OrganiserMenu(QWidget):
    def __init__(self, mainWindow, uname, upref):
        QWidget.__init__(self, None)
        layout = QVBoxLayout()
        self.mainWindows = mainWindow
        self.uname = uname
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.logout.clicked.connect(self.Logout)
        self.ui.profile.clicked.connect(self.Profile)
        self.ui.create.clicked.connect(self.CreateCourse)
        self.ui.display.clicked.connect(self.OrgViewAll)
        self.ui.delete_2.clicked.connect(self.OrgDel)

    def Logout(self):
        self.hide()
        self.mainWindows.show()

    def Profile(self):
        self.hide()
        self.prof = OrgProfile(self)
        self.prof.show()

    def CreateCourse(self):
        self.hide()
        self.create = OrgCreate(self, self.uname)
        self.create.show()

    def OrgViewAll(self):
        self.hide()
        self.viewall = OrgViewAll(self, self.uname)
        self.viewall.show()

    def OrgDel(self):
        self.hide()
        self.eliminate = OrgDelete(self, self.uname)
        self.eliminate.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrganiserMenu()
    w.show()
    sys.exit(app.exec_())