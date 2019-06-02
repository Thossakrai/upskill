import sys

from controller.OrgUpdateProfile import OrgImproveProfile
from screen.LrnProfile import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class LrnProfile(QWidget):
    def __init__(self,LearnerViewEnrolledCourseWindow):
        QWidget.__init__(self, None)
        self.viewenrolledWindow = LearnerViewEnrolledCourseWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Go_back.clicked.connect(self.goback)
        self.ui.EditProf.clicked.connect(self.editdetail)

    def goback(self):
        self.hide()
        self.viewenrolledWindow.show()

    def editdetail(self):
        self.hide()
        self.EditProf = OrgImproveProfile(self)
        self.EditProf.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnProfile()
    w.show()
    sys.exit(app.exec_())