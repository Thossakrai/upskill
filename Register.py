import sys

from screen.orgreg import Ui_Form
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from backend.signupsystem import *
from PySide2.QtMultimedia import QSound


class Register(QWidget):
    def __init__(self,mainWindow, utype):
        QWidget.__init__(self, None)
        self.mainWindow = mainWindow
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.utype = utype
        self.ui.Signup_2.clicked.connect(self.GoBack)
        self.ui.Signup.clicked.connect(self.SignUp)

    def GoBack(self):
        self.hide()
        self.mainWindow.show()

    def SignUp(self):
        fname = self.ui.Fname.text()
        lname = self.ui.Lname.text()
        birthdate = self.ui.Date.text()
        gender = self.ui.Sex.currentText()
        print(gender)
        uname = self.ui.User.text()
        phone = self.ui.User_2.text()
        email = self.ui.User_3.text()
        upref = self.ui.type.currentText()
        pw = self.ui.Password.text()
        self.signupsystem = SignUpSystem(fname, lname, birthdate, gender, uname, pw, phone, email, upref, self.utype)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Register()
    w.show()
    sys.exit(app.exec_())
