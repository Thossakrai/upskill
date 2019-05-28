from screen.signin import Ui_Form
import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound


class SignInUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Menu")
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SignInUI()
    w.show()
    sys.exit(app.exec_())
    