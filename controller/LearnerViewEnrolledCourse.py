import sys

from controller.LearnerConfirmCancel import LrnConfirmCancel
from controller.LearnerEditPref import LrnEditPref
from screen.viewallenrollment import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class LrnViewEnrolled(QWidget):
    def __init__(self,LearnerMenuWindow, learner):
        QWidget.__init__(self, None)
        self.menuWindow = LearnerMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goback)
        self.ui.pushButton_2.clicked.connect(self.editdetail)
        self.ui.pushButton_3.clicked.connect(self.cancel)
        self.learner = learner
        self.getCourses()

    def goback(self):
        self.hide()
        self.menuWindow.show()

    def editdetail(self):
        self.hide()
        self.EditPref = LrnEditPref(self)
        self.EditPref.show()

    def cancel(self):
        # self.hide()
        self.remove = LrnConfirmCancel(self, self.learner)
        self.remove.show()

    def getCourses(self):
        enrolled_courses = self.learner.getEnrolledCourses()
        self.ui.tableView.setModel(enrolled_courses)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnViewEnrolled()
    w.show()
    sys.exit(app.exec_())