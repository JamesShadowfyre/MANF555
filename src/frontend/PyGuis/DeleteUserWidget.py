# -*- coding: utf-8 -*-
# Delete User GUI
# Form implementation generated from reading ui file 'ChangePasswordWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordWidget(object):
    def setupUi(self, ChangePasswordWidget):
        ChangePasswordWidget.setObjectName("ChangePasswordWidget")
        ChangePasswordWidget.resize(316, 170)
        self.changePasswordGroupBox = QtWidgets.QGroupBox(ChangePasswordWidget)
        self.changePasswordGroupBox.setGeometry(QtCore.QRect(10, 10, 300, 150))
        self.changePasswordGroupBox.setObjectName("changePasswordGroupBox")
        self.savePasswordButton = QtWidgets.QPushButton(self.changePasswordGroupBox)
        self.savePasswordButton.setGeometry(QtCore.QRect(70, 120, 141, 24))
        self.savePasswordButton.setObjectName("savePasswordButton")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.changePasswordGroupBox)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 261, 101))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.changePasswordPassword = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.changePasswordPassword.setObjectName("changePasswordPassword")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.changePasswordPassword)
        self.changePasswordUsername = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.changePasswordUsername.setObjectName("changePasswordUsername")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.changePasswordUsername)
        self.changePasswordEmployeeNumber = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.changePasswordEmployeeNumber.setObjectName("changePasswordEmployeeNumber")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.changePasswordEmployeeNumber)

        self.retranslateUi(ChangePasswordWidget)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordWidget)

    def retranslateUi(self, ChangePasswordWidget):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordWidget.setWindowTitle(_translate("ChangePasswordWidget", "Delete User"))
        self.changePasswordGroupBox.setTitle(_translate("ChangePasswordWidget", "Delete User"))
        self.savePasswordButton.setText(_translate("ChangePasswordWidget", "Delete User"))
        self.label_12.setText(_translate("ChangePasswordWidget", "Employee Number"))
        self.label_10.setText(_translate("ChangePasswordWidget", "Username"))
        self.label_11.setText(_translate("ChangePasswordWidget", "Password"))
        self.changePasswordUsername.setPlaceholderText(_translate("ChangePasswordWidget", "Auto-fill from User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePasswordWidget = QtWidgets.QWidget()
    ui = Ui_ChangePasswordWidget()
    ui.setupUi(ChangePasswordWidget)
    ChangePasswordWidget.show()
    sys.exit(app.exec_())