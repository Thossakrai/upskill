import sys

from screen.OrgDeleteCourse import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from OrganiserViewACourse import *


class OrgDelete(QWidget):
    def __init__(self,OrganiserMenuWindow, uname):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        self.uname = uname
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.course = Course()
        self.getCourses()



    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def getCourses(self):
        self.courses = self.course.viewCourse(self.uname)


    def deleteCourse(self):
        self.title = "Java"
        self.course.deleteCourse(self.uname, self.title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgDelete()
    w.show()
    sys.exit(app.exec_())