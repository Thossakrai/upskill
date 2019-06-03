import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from controller.Organiser.OrgConfirmDelCourse import OrgConfirmDelete
from screen.DeleteCourse import Ui_Form


class OrgDelete(QWidget):
    def __init__(self,OrganiserMenuWindow, org):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        self.org = org
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.goback)
        self.getCourses()
        self.ui.deleted.clicked.connect(self.godelete)

    def goback(self):
        self.hide()
        self.orgmenuWindow.show()


    def getCourses(self):
        self.courses = self.org.viewCourse()
        self.ui.tableView.setModel(self.courses)


    def godelete(self):
        # self.hide()
        self.godel = OrgConfirmDelete(self, self.org)
        self.godel.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgDelete()
    w.show()
    sys.exit(app.exec_())