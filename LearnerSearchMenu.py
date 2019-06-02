import sys

from screen.search_result import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from backend.course import *
from backend.User import *


class LrnSearch(QWidget):
    def __init__(self, LearnerViewEnrolledCourseWindow, upref, uname):
        QWidget.__init__(self, None)
        self.viewenrolledWindow = LearnerViewEnrolledCourseWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.upref = upref
        self.uname = uname
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.searchCourse)
        self.ui.pushButton_3.clicked.connect(self.goback)
        self.ui.tableView.clicked.connect(self.enroll)
        self.browseCourse()

    def goback(self):
        self.hide()
        self.viewenrolledWindow.show()

    def enroll(self, item):
        print(item.column(), item.row())
        enrolled_course_title = self.courses.record(item.row()).value("TITLE")
        enrolled_course_speaker = self.courses.record(item.row()).value("SPEAKER")
        print(enrolled_course_speaker)
        print(self.courses.record(item.row()))
        self.learner = Learner(self.uname)
        self.learner.enroll(enrolled_course_title, enrolled_course_speaker)

    def browseCourse(self):
        self.course = Course()
        self.courses = self.course.browse(self.upref)
        self.ui.tableView.setModel(self.courses)

    def searchCourse(self):
        self.search_text = self.ui.lineEdit.text()
        self.course = Course()
        self.courses = self.course.search(self.search_text)
        self.ui.tableView.setModel(self.courses)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnSearch()
    w.show()
    sys.exit(app.exec_())
