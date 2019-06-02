import sys

from controller.OrgConfirmDelCourse import OrgConfirmDelete
# from screen.OrgDeleteCourse import Ui_Form
from screen.DeleteCourse import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
#from OrganiserViewACourse import *
from backend.course import *


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
        self.ui.deleted.clicked.connect(self.godelete)

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()


    def getCourses(self):
        self.courses = self.course.viewCourse(self.uname)
        self.ui.tableView.setModel(self.courses)


    def deleteCourse(self):
        self.title = "Java"
        self.course.deleteCourse(self.uname, self.title)

    def godelete(self):
        # self.hide()
        self.godel = OrgConfirmDelete(self, self.uname)
        self.godel.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgDelete()
    w.show()
    sys.exit(app.exec_())