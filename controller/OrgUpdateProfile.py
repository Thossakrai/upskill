import sys

from controller.EditLearnerProfile import EditLrnProf
from screen.OrgUpdateProf import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class OrgImproveProfile(QWidget):
    def __init__(self,OrganiserMenuWindow):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.ui.save.clicked.connect(self.updateinfo)

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def updateinfo(self):
        self.hide()
        self.orgmenuWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgImproveProfile()
    w.show()
    sys.exit(app.exec_())