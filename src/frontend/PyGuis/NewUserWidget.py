# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUserWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newUserWidget(object):
    def setupUi(self, newUserWidget):
        newUserWidget.setObjectName("newUserWidget")
        newUserWidget.resize(304, 209)
        self.newUserGroupBox = QtWidgets.QGroupBox(newUserWidget)
        self.newUserGroupBox.setGeometry(QtCore.QRect(10, 10, 300, 175))
        self.newUserGroupBox.setObjectName("newUserGroupBox")
        self.saveNewUserButton = QtWidgets.QPushButton(self.newUserGroupBox)
        self.saveNewUserButton.setGeometry(QtCore.QRect(100, 150, 75, 24))
        self.saveNewUserButton.setObjectName("saveNewUserButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.newUserGroupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.newUserUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.newUserUsername.setObjectName("newUserUsername")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.newUserUsername)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.editUserRights_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.editUserRights_2.setObjectName("editUserRights_2")
        self.editUserRights_2.addItem("")
        self.editUserRights_2.addItem("")
        self.editUserRights_2.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editUserRights_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.retranslateUi(newUserWidget)
        QtCore.QMetaObject.connectSlotsByName(newUserWidget)


    def retranslateUi(self, newUserWidget):
        _translate = QtCore.QCoreApplication.translate
        newUserWidget.setWindowTitle(_translate("newUserWidget", "New User"))
        self.newUserGroupBox.setTitle(_translate("newUserWidget", "New User"))
        self.saveNewUserButton.setText(_translate("newUserWidget", "Save"))
        self.label_3.setText(_translate("newUserWidget", "Employee Number"))
        self.label.setText(_translate("newUserWidget", "Username"))
        self.label_17.setText(_translate("newUserWidget", "Rights"))
        self.editUserRights_2.setItemText(0, _translate("newUserWidget", "---"))
        self.editUserRights_2.setItemText(1, _translate("newUserWidget", "Admin"))
        self.editUserRights_2.setItemText(2, _translate("newUserWidget", "User"))
        self.label_2.setText(_translate("newUserWidget", "Password"))
