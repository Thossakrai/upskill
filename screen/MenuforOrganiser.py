import sys
import random
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtMultimedia import QSound
from Menu import Ui_Form    # Use the name of py files eg. Menu.py

class Menufororg(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.setWindowTitle("Menu")

        self.ui = Ui_Form()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Menufororg()
    w.show()
    sys.exit(app.exec_())