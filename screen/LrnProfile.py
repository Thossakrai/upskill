# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lrn_profile.ui',
# licensing of 'lrn_profile.ui' applies.
#
# Created: Mon Jun  3 01:16:55 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 170, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 170, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 255, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 170, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(101, 127, 126))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.389, 0.357727, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(150, 165, 220))
        gradient.setColorAt(1.0, QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 255, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        Form.setPalette(palette)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: qlineargradient(spread:repeat, x1:0.389, y1:0.357727, x2:1, y2:1, stop:0 rgba(150, 165, 220, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 641, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.EditProf = QtWidgets.QPushButton(Form)
        self.EditProf.setGeometry(QtCore.QRect(640, 500, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EditProf.setFont(font)
        self.EditProf.setStyleSheet("QPushButton{\n"
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
        self.EditProf.setObjectName("EditProf")
        self.Go_back = QtWidgets.QPushButton(Form)
        self.Go_back.setGeometry(QtCore.QRect(640, 610, 411, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Go_back.setFont(font)
        self.Go_back.setStyleSheet("QPushButton{\n"
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
        self.Go_back.setObjectName("Go_back")
        self.Fname_title = QtWidgets.QLabel(Form)
        self.Fname_title.setGeometry(QtCore.QRect(30, 190, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_title.setFont(font)
        self.Fname_title.setStyleSheet("background-color: transparent")
        self.Fname_title.setObjectName("Fname_title")
        self.Fname_2 = QtWidgets.QLabel(Form)
        self.Fname_2.setGeometry(QtCore.QRect(30, 260, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_2.setFont(font)
        self.Fname_2.setStyleSheet("background-color: transparent")
        self.Fname_2.setObjectName("Fname_2")
        self.Fname_3 = QtWidgets.QLabel(Form)
        self.Fname_3.setGeometry(QtCore.QRect(30, 110, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_3.setFont(font)
        self.Fname_3.setStyleSheet("background-color: transparent")
        self.Fname_3.setObjectName("Fname_3")
        self.Fname_4 = QtWidgets.QLabel(Form)
        self.Fname_4.setGeometry(QtCore.QRect(30, 330, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_4.setFont(font)
        self.Fname_4.setStyleSheet("background-color: transparent")
        self.Fname_4.setObjectName("Fname_4")
        self.Fname_5 = QtWidgets.QLabel(Form)
        self.Fname_5.setGeometry(QtCore.QRect(30, 470, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_5.setFont(font)
        self.Fname_5.setStyleSheet("background-color: transparent")
        self.Fname_5.setObjectName("Fname_5")
        self.Fname_6 = QtWidgets.QLabel(Form)
        self.Fname_6.setGeometry(QtCore.QRect(30, 400, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_6.setFont(font)
        self.Fname_6.setStyleSheet("background-color: transparent")
        self.Fname_6.setObjectName("Fname_6")
        self.Fname_7 = QtWidgets.QLabel(Form)
        self.Fname_7.setGeometry(QtCore.QRect(30, 610, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_7.setFont(font)
        self.Fname_7.setStyleSheet("background-color: transparent")
        self.Fname_7.setObjectName("Fname_7")
        self.Fname_8 = QtWidgets.QLabel(Form)
        self.Fname_8.setGeometry(QtCore.QRect(30, 540, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Fname_8.setFont(font)
        self.Fname_8.setStyleSheet("background-color: transparent")
        self.Fname_8.setObjectName("Fname_8")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(650, 310, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(100)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {\n"
"color: #8F7B45;\n"
"border-color: black;\n"
"\n"
"background-color: transparent;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(650, 20, 441, 321))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(150)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("QLabel {\n"
"color: #8F7B45;\n"
"background-color: transparent;\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.Uname = QtWidgets.QLabel(Form)
        self.Uname.setGeometry(QtCore.QRect(200, 110, 501, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Uname.setFont(font)
        self.Uname.setStyleSheet("background-color: transparent")
        self.Uname.setObjectName("Uname")
        self.Fname = QtWidgets.QLabel(Form)
        self.Fname.setGeometry(QtCore.QRect(200, 190, 501, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Fname.setFont(font)
        self.Fname.setStyleSheet("background-color: transparent")
        self.Fname.setObjectName("Fname")
        self.Lname = QtWidgets.QLabel(Form)
        self.Lname.setGeometry(QtCore.QRect(200, 260, 491, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Lname.setFont(font)
        self.Lname.setStyleSheet("background-color: transparent")
        self.Lname.setObjectName("Lname")
        self.Sex = QtWidgets.QLabel(Form)
        self.Sex.setGeometry(QtCore.QRect(200, 330, 511, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Sex.setFont(font)
        self.Sex.setStyleSheet("background-color: transparent")
        self.Sex.setObjectName("Sex")
        self.Email = QtWidgets.QLabel(Form)
        self.Email.setGeometry(QtCore.QRect(200, 400, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Email.setFont(font)
        self.Email.setStyleSheet("background-color: transparent")
        self.Email.setObjectName("Email")
        self.Phone = QtWidgets.QLabel(Form)
        self.Phone.setGeometry(QtCore.QRect(200, 470, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Phone.setFont(font)
        self.Phone.setStyleSheet("background-color: transparent")
        self.Phone.setObjectName("Phone")
        self.Type = QtWidgets.QLabel(Form)
        self.Type.setGeometry(QtCore.QRect(200, 540, 351, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Type.setFont(font)
        self.Type.setStyleSheet("background-color: transparent")
        self.Type.setObjectName("Type")
        self.Pref = QtWidgets.QLabel(Form)
        self.Pref.setGeometry(QtCore.QRect(200, 610, 351, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.Pref.setFont(font)
        self.Pref.setStyleSheet("background-color: transparent")
        self.Pref.setObjectName("Pref")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Learner\'s Profile", None, -1))
        self.EditProf.setText(QtWidgets.QApplication.translate("Form", "Edit Profile", None, -1))
        self.Go_back.setText(QtWidgets.QApplication.translate("Form", "Go back", None, -1))
        self.Fname_title.setText(QtWidgets.QApplication.translate("Form", "First name:", None, -1))
        self.Fname_2.setText(QtWidgets.QApplication.translate("Form", "Last name:", None, -1))
        self.Fname_3.setText(QtWidgets.QApplication.translate("Form", "Username:", None, -1))
        self.Fname_4.setText(QtWidgets.QApplication.translate("Form", "Gender:", None, -1))
        self.Fname_5.setText(QtWidgets.QApplication.translate("Form", "Phone No:", None, -1))
        self.Fname_6.setText(QtWidgets.QApplication.translate("Form", "Email:", None, -1))
        self.Fname_7.setText(QtWidgets.QApplication.translate("Form", "Preference: ", None, -1))
        self.Fname_8.setText(QtWidgets.QApplication.translate("Form", "Type:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "skill", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "UP", None, -1))
        self.Uname.setText(QtWidgets.QApplication.translate("Form", "uname", None, -1))
        self.Fname.setText(QtWidgets.QApplication.translate("Form", "Fname", None, -1))
        self.Lname.setText(QtWidgets.QApplication.translate("Form", "Lname", None, -1))
        self.Sex.setText(QtWidgets.QApplication.translate("Form", "Sex", None, -1))
        self.Email.setText(QtWidgets.QApplication.translate("Form", "Email", None, -1))
        self.Phone.setText(QtWidgets.QApplication.translate("Form", "Phone", None, -1))
        self.Type.setText(QtWidgets.QApplication.translate("Form", "Type", None, -1))
        self.Pref.setText(QtWidgets.QApplication.translate("Form", "Pref", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

