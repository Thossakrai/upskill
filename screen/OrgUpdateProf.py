# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateprofile.ui',
# licensing of 'updateprofile.ui' applies.
#
# Created: Wed May 29 18:07:56 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 247, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 120, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 160, 145))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 247, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 247, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 120, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 160, 145))
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 247, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 120, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 247, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 120, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 160, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 120, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 120, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 240, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.save = QtWidgets.QPushButton(self.widget)
        self.save.setGeometry(QtCore.QRect(540, 590, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setGeometry(QtCore.QRect(30, 590, 471, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.Lname_2 = QtWidgets.QLineEdit(self.widget)
        self.Lname_2.setGeometry(QtCore.QRect(780, 50, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Lname_2.setFont(font)
        self.Lname_2.setText("")
        self.Lname_2.setObjectName("Lname_2")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setGeometry(QtCore.QRect(10, 40, 261, 181))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(100)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_26.setFont(font)
        self.label_26.setAutoFillBackground(False)
        self.label_26.setStyleSheet("QLabel {\n"
"color: rgb(0, 12, 150);\n"
"}")
        self.label_26.setObjectName("label_26")
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setGeometry(QtCore.QRect(30, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setGeometry(QtCore.QRect(540, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.User_4 = QtWidgets.QLineEdit(self.widget)
        self.User_4.setGeometry(QtCore.QRect(540, 320, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.User_4.setFont(font)
        self.User_4.setText("")
        self.User_4.setObjectName("User_4")
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setGeometry(QtCore.QRect(230, 60, 271, 181))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(70)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel {\n"
"color: rgb(0, 12, 150);\n"
"}")
        self.label_20.setObjectName("label_20")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(780, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.Fname_2 = QtWidgets.QLineEdit(self.widget)
        self.Fname_2.setGeometry(QtCore.QRect(540, 50, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Fname_2.setFont(font)
        self.Fname_2.setStyleSheet("setStyleSheet(\"QLineEdit[readOnly=\"true\"])")
        self.Fname_2.setText("")
        self.Fname_2.setObjectName("Fname_2")
        self.type_2 = QtWidgets.QComboBox(self.widget)
        self.type_2.setGeometry(QtCore.QRect(30, 510, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.type_2.setFont(font)
        self.type_2.setObjectName("type_2")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.type_2.addItem("")
        self.User_6 = QtWidgets.QLineEdit(self.widget)
        self.User_6.setGeometry(QtCore.QRect(540, 230, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.User_6.setFont(font)
        self.User_6.setText("")
        self.User_6.setObjectName("User_6")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setGeometry(QtCore.QRect(30, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(20, 180, 481, 101))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(35)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
"color: rgb(0, 12, 150);\n"
"}")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(540, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.Pref_3 = QtWidgets.QLineEdit(self.widget)
        self.Pref_3.setGeometry(QtCore.QRect(540, 410, 471, 151))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Pref_3.setFont(font)
        self.Pref_3.setObjectName("Pref_3")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setGeometry(QtCore.QRect(30, 470, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setGeometry(QtCore.QRect(540, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(780, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setGeometry(QtCore.QRect(540, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setGeometry(QtCore.QRect(540, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.Password_2 = QtWidgets.QLineEdit(self.widget)
        self.Password_2.setGeometry(QtCore.QRect(30, 410, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Password_2.setFont(font)
        self.Password_2.setText("")
        self.Password_2.setObjectName("Password_2")
        self.Date_2 = QtWidgets.QDateEdit(self.widget)
        self.Date_2.setGeometry(QtCore.QRect(540, 140, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Date_2.setFont(font)
        self.Date_2.setObjectName("Date_2")
        self.User_5 = QtWidgets.QLineEdit(self.widget)
        self.User_5.setGeometry(QtCore.QRect(30, 320, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.User_5.setFont(font)
        self.User_5.setText("")
        self.User_5.setObjectName("User_5")
        self.Sex_2 = QtWidgets.QComboBox(self.widget)
        self.Sex_2.setGeometry(QtCore.QRect(780, 140, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.Sex_2.setFont(font)
        self.Sex_2.setObjectName("Sex_2")
        self.Sex_2.addItem("")
        self.Sex_2.setItemText(0, "Gender")
        self.Sex_2.addItem("")
        self.Sex_2.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.save.setText(QtWidgets.QApplication.translate("Form", "Save and Return", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("Form", "Do not save and Go back", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("Form", "UP", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", "Profile Details", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("Form", "skill", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "Last Name", None, -1))
        self.type_2.setItemText(0, QtWidgets.QApplication.translate("Form", "None", None, -1))
        self.type_2.setItemText(1, QtWidgets.QApplication.translate("Form", "Academic", None, -1))
        self.type_2.setItemText(2, QtWidgets.QApplication.translate("Form", "Art", None, -1))
        self.type_2.setItemText(3, QtWidgets.QApplication.translate("Form", "Cooking", None, -1))
        self.type_2.setItemText(4, QtWidgets.QApplication.translate("Form", "Community Service", None, -1))
        self.type_2.setItemText(5, QtWidgets.QApplication.translate("Form", "Culture", None, -1))
        self.type_2.setItemText(6, QtWidgets.QApplication.translate("Form", "Dance", None, -1))
        self.type_2.setItemText(7, QtWidgets.QApplication.translate("Form", "Exercise", None, -1))
        self.type_2.setItemText(8, QtWidgets.QApplication.translate("Form", "Gambling", None, -1))
        self.type_2.setItemText(9, QtWidgets.QApplication.translate("Form", "Gaming", None, -1))
        self.type_2.setItemText(10, QtWidgets.QApplication.translate("Form", "Indoor", None, -1))
        self.type_2.setItemText(11, QtWidgets.QApplication.translate("Form", "Knitting", None, -1))
        self.type_2.setItemText(12, QtWidgets.QApplication.translate("Form", "Music", None, -1))
        self.type_2.setItemText(13, QtWidgets.QApplication.translate("Form", "Photography", None, -1))
        self.type_2.setItemText(14, QtWidgets.QApplication.translate("Form", "Science", None, -1))
        self.type_2.setItemText(15, QtWidgets.QApplication.translate("Form", "Sport", None, -1))
        self.type_2.setItemText(16, QtWidgets.QApplication.translate("Form", "Outdoor", None, -1))
        self.type_2.setItemText(17, QtWidgets.QApplication.translate("Form", "Volunteer", None, -1))
        self.type_2.setItemText(18, QtWidgets.QApplication.translate("Form", "Yoga", None, -1))
        self.type_2.setItemText(19, QtWidgets.QApplication.translate("Form", "Zen", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Registration Form", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Form", "Phone Number", None, -1))
        self.Pref_3.setText(QtWidgets.QApplication.translate("Form", "Profile Details", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", "Preference Types", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("Form", "Email Address", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "Gender", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "First Name", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Form", "DOB", None, -1))
        self.Sex_2.setItemText(1, QtWidgets.QApplication.translate("Form", "Male", None, -1))
        self.Sex_2.setItemText(2, QtWidgets.QApplication.translate("Form", "Female", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

