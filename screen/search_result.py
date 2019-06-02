# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Searchresult.ui',
# licensing of 'Searchresult.ui' applies.
#
# Created: Sun Jun  2 18:26:33 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        Form.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 165, 220, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(830, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"color: #black;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #FFE9AD);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1.5px;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1.5px solid black;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #B39A56, stop: 1 #FFE9AD);\n"
"}\n"
"\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 541, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(600, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"color: #black;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 #FFE9AD);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1.5px;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1.5px solid black;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #B39A56, stop: 1 #FFE9AD);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(30, 110, 1011, 581))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "Go back", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Search Course by Text", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Search", None, -1))

