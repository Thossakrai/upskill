import sys

from OrgConfirmDelCourse import OrgConfirmDelete
from screen.OrgDeleteCourse import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class OrgDelete(QWidget):
    def __init__(self,OrganiserMenuWindow):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.ui.deleted.clicked.connect(self.godelete)

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()

    def godelete(self):
        self.hide()
        self.godel = OrgConfirmDelete(self)
        self.godel.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgDelete()
    w.show()
    sys.exit(app.exec_())