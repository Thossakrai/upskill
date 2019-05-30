import sys

from screen.LrnDisplayCSearch import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class LrnSearch(QWidget):
    def __init__(self,LearnerViewEnrolledCourseWindow):
        QWidget.__init__(self, None)
        self.viewenrolledWindow = LearnerViewEnrolledCourseWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goback)

    def goback(self):
        self.hide()
        self.viewenrolledWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LrnSearch()
    w.show()
    sys.exit(app.exec_())