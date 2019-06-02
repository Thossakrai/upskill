import sys

from controller.OrgUpdateProfile import OrgImproveProfile
from controller.EditLearnerProfile import EditLrnProf
from screen.viewprofileorg import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class OrgProfile(QWidget):
    def __init__(self,OrganiserMenuWindow):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.goback)
        self.ui.pushButton_3.clicked.connect(self.edit)

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def edit(self):
        self.hide()
        self.improve = OrgImproveProfile(self)
        self.improve.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgProfile()
    w.show()
    sys.exit(app.exec_())