import sys

from screen.PunpunViewallcourses import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from backend.course import Course


class OrgViewAll(QWidget):
    def __init__(self,OrganiserMenuWindow, uname):
        QWidget.__init__(self, None)
        self.orgmenuWindow = OrganiserMenuWindow
        self.uname = uname
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goback)
        self.getCourses()
        self.ui.pushButton_2.clicked.connect(self.getCourses)


    def goback(self):
        self.hide()
        self.orgmenuWindow.show()


    def getCourses(self, ):
        self.course = Course()
        ##return all courses that user creted
        self.courses = self.course.viewCourse(self.uname)
        print(self.courses)
        self.updateUI(self.courses)
        return self.courses



    def updateUI(self, courses):
        self.ui.tableView.setModel(courses)
        self.ui.tableView.show()



    """
    def showCourse(self, ): # try to display
        for d in self.courses:
            row = []
            for name in d:
                item = QStandardItem(name)
                item.setEditable(False)
                row.append(item)
            self.course.appendRow(row)
    """



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = OrgViewAll()
    w.show()
    sys.exit(app.exec_())