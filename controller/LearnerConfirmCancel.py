import sys

from screen.LrnConfirmCancel import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from backend.course import *


class LrnConfirmCancel(QWidget):
    def __init__(self,OrganiserMenuWindow, learner):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.ui.deleted.clicked.connect(self.removed)
        self.learner = learner

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def removed(self):
        removed_course = self.ui.lineEdit.text()
        isCompleteRemove = self.learner.cancelEnrollment(removed_course)
        if isCompleteRemove :
            self.hide()
            self.orgmenuWindow.getCourses()
            self.orgmenuWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnConfirmCancel()
    w.show()
    sys.exit(app.exec_())