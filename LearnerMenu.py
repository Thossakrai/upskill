import sys

from LearnerProfile import LrnProfile
from LearnerViewEnrolledCourse import LrnViewEnrolled
from screen.LrnMenu import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class LearnerMenu(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self, None)
        self.mainWindow = mainWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.Logout)
        self.ui.pushButton.clicked.connect(self.ViewEnrolled)
        self.ui.pushButton_3.clicked.connect(self.Profile)

    def Logout(self):
        self.hide()
        self.mainWindow.show()

    def ViewEnrolled(self):
        self.hide()
        self.LrnView = LrnViewEnrolled(self)
        self.LrnView.show()

    def Profile(self):
        self.hide()
        self.prof = LrnProfile(self)
        self.prof.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LearnerMenu()
    w.show()
    sys.exit(app.exec_())