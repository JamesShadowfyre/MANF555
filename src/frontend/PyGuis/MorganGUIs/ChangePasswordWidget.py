# Form implementation generated from reading ui file 'ChangePasswordWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordWidget(object):
    def setupUi(self, ChangePasswordWidget):
        ChangePasswordWidget.setObjectName("ChangePasswordWidget")
        ChangePasswordWidget.resize(316, 170)
        self.changePasswordGroupBox = QtWidgets.QGroupBox(parent=ChangePasswordWidget)
        self.changePasswordGroupBox.setGeometry(QtCore.QRect(10, 10, 300, 150))
        self.changePasswordGroupBox.setObjectName("changePasswordGroupBox")
        self.savePasswordButton = QtWidgets.QPushButton(parent=self.changePasswordGroupBox)
        self.savePasswordButton.setGeometry(QtCore.QRect(70, 120, 141, 24))
        self.savePasswordButton.setObjectName("savePasswordButton")
        self.formLayoutWidget_4 = QtWidgets.QWidget(parent=self.changePasswordGroupBox)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 261, 101))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.formLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.changePasswordPassword = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.changePasswordPassword.setObjectName("changePasswordPassword")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.changePasswordPassword)
        self.changePasswordEmployeeNumber = QtWidgets.QLineEdit(parent=self.formLayoutWidget_4)
        self.changePasswordEmployeeNumber.setObjectName("changePasswordEmployeeNumber")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.changePasswordEmployeeNumber)
        self.changePasswordUsername = QtWidgets.QComboBox(parent=self.formLayoutWidget_4)
        self.changePasswordUsername.setObjectName("changePasswordUsername")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.changePasswordUsername)

        self.retranslateUi(ChangePasswordWidget)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordWidget)

    def retranslateUi(self, ChangePasswordWidget):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordWidget.setWindowTitle(_translate("ChangePasswordWidget", "Change Password"))
        self.changePasswordGroupBox.setTitle(_translate("ChangePasswordWidget", "Change Password"))
        self.savePasswordButton.setText(_translate("ChangePasswordWidget", "Save Password"))
        self.label_12.setText(_translate("ChangePasswordWidget", "Employee Number"))
        self.label_10.setText(_translate("ChangePasswordWidget", "Username"))
        self.label_11.setText(_translate("ChangePasswordWidget", "Password"))
        self.changePasswordEmployeeNumber.setPlaceholderText(_translate("ChangePasswordWidget", "Auto-fill from User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePasswordWidget = QtWidgets.QWidget()
    ui = Ui_ChangePasswordWidget()
    ui.setupUi(ChangePasswordWidget)
    ChangePasswordWidget.show()
    sys.exit(app.exec())
