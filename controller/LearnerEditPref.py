import sys

from screen.LrnEditDetails import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from backend.User import Learner


class LrnEditPref(QWidget):
    def __init__(self,LearnerViewEnrolledCourse):
        QWidget.__init__(self, None)
        self.LrnViewEnrolled = LearnerViewEnrolledCourse
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.goback)


    def goback(self):
        self.hide()
        self.LrnViewEnrolled.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnEditPref()
    w.show()
    sys.exit(app.exec_())