import sys

from screen.OrgCreateCourse import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sqlite3
from PySide2.QtMultimedia import QSound
from backend.course import *


class OrgCreate(QWidget):
    def __init__(self,OrganiserMenuWindow, uname):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        self.uname =  uname
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.ui.save.clicked.connect(self.createCourse)


    def goback(self):
        self.hide()
        self.orgmenuWindow.show()


    def createCourse(self):
        self.title = self.ui.title.text()
        self.speaker = self.ui.speaker.text()
        self.dateline = self.ui.datetime.text()
        self.location = self.ui.location.text()
        self.tag = self.ui.tag.text()
        self.type = self.ui.type.currentText()
        self.details = self.ui.details.text()
        self.course = Course()
        created = self.course.createCourse(self.title, self.speaker, self.dateline, self.location, self.tag, self.type, self.details, self.uname)
        if created :
            self.hide()
            self.orgmenuWindow.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgCreate()
    w.show()
    sys.exit(app.exec_())