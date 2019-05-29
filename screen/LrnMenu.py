# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchMenu.ui',
# licensing of 'SearchMenu.ui' applies.
#
# Created: Wed May 29 14:45:08 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(780, 150, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 280, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 20, 281, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.Pref = QtWidgets.QLineEdit(Form)
        self.Pref.setGeometry(QtCore.QRect(20, 120, 731, 271))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Pref.setFont(font)
        self.Pref.setObjectName("Pref")
        self.Pref_2 = QtWidgets.QLineEdit(Form)
        self.Pref_2.setGeometry(QtCore.QRect(20, 420, 1041, 271))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Pref_2.setFont(font)
        self.Pref_2.setObjectName("Pref_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "Search", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "View Course", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "Logout", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "Profile", None, -1))
        self.Pref.setText(QtWidgets.QApplication.translate("Form", "Newest Courses", None, -1))
        self.Pref_2.setText(QtWidgets.QApplication.translate("Form", "Just for you Courses", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

