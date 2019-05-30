import sys

from screen.LrnDisplayCSearch import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from backend.course import *


class LrnSearch(QWidget):
    def __init__(self,LearnerViewEnrolledCourseWindow, upref):
        QWidget.__init__(self, None)
        self.viewenrolledWindow = LearnerViewEnrolledCourseWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.upref = upref
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goback)
        self.browseCourse()



    def goback(self):
        self.hide()
        self.viewenrolledWindow.show()


    def browseCourse(self):
        self.course = Course()
        ##return courses match to the user preferences##
        self.courses = self.course.browse(self.upref)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnSearch()
    w.show()
    sys.exit(app.exec_())