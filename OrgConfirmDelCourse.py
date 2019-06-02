import sys

from screen.OrgConfirmDel import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from backend.course import *


class OrgConfirmDelete(QWidget):
    def __init__(self,OrganiserMenuWindow, uname):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.uname = uname
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.ui.deleted.clicked.connect(self.removed)

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def removed(self):
        self.c = Course()
        self.course_title = self.ui.lineEdit.text()
        self.c.deleteCourse(self.uname, self.course_title)
        self.hide()
        self.orgmenuWindow.getCourses()
        self.orgmenuWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgConfirmDelete()
    w.show()
    sys.exit(app.exec_())