# Form implementation generated from reading ui file 'editCustomerWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditCustomerWidget(object):
    def setupUi(self, EditCustomerWidget):
        EditCustomerWidget.setObjectName("EditCustomerWidget")
        EditCustomerWidget.resize(504, 484)
        self.editCustomerButton = QtWidgets.QPushButton(parent=EditCustomerWidget)
        self.editCustomerButton.setGeometry(QtCore.QRect(190, 400, 141, 24))
        self.editCustomerButton.setObjectName("editCustomerButton")
        self.groupBox = QtWidgets.QGroupBox(parent=EditCustomerWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 481, 381))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 461, 331))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.accountInformationLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.accountInformationLayout.setContentsMargins(0, 0, 0, 0)
        self.accountInformationLayout.setObjectName("accountInformationLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.accountInformationLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.editCustomerAccountSelectionBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.editCustomerAccountSelectionBox.setObjectName("editCustomerAccountSelectionBox")
        self.editCustomerAccountSelectionBox.addItem("")
        self.editCustomerAccountSelectionBox.addItem("")
        self.editCustomerAccountSelectionBox.addItem("")
        self.editCustomerAccountSelectionBox.addItem("")
        self.accountInformationLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerAccountSelectionBox)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.accountInformationLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.editCustomerId = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerId.setObjectName("editCustomerId")
        self.accountInformationLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerId)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.accountInformationLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.editCustomerStreetAddressLine1 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerStreetAddressLine1.setObjectName("editCustomerStreetAddressLine1")
        self.accountInformationLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerStreetAddressLine1)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.accountInformationLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.editCustomerStreetAddressLine2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerStreetAddressLine2.setObjectName("editCustomerStreetAddressLine2")
        self.accountInformationLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerStreetAddressLine2)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.accountInformationLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.editCustomerCity = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerCity.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.editCustomerCity.setObjectName("editCustomerCity")
        self.accountInformationLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerCity)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.accountInformationLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.editCustomerRegion = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerRegion.setObjectName("editCustomerRegion")
        self.accountInformationLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerRegion)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.accountInformationLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.editCustomerPostalCode = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerPostalCode.setObjectName("editCustomerPostalCode")
        self.accountInformationLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerPostalCode)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.accountInformationLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.editCustomerCountry = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerCountry.setObjectName("editCustomerCountry")
        self.accountInformationLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerCountry)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.accountInformationLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.editCustomerPhoneNumber = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerPhoneNumber.setObjectName("editCustomerPhoneNumber")
        self.accountInformationLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerPhoneNumber)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.accountInformationLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.editCustomerEmail = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.editCustomerEmail.setObjectName("editCustomerEmail")
        self.accountInformationLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editCustomerEmail)

        self.retranslateUi(EditCustomerWidget)
        QtCore.QMetaObject.connectSlotsByName(EditCustomerWidget)

    def retranslateUi(self, EditCustomerWidget):
        _translate = QtCore.QCoreApplication.translate
        EditCustomerWidget.setWindowTitle(_translate("EditCustomerWidget", "Edit Customer"))
        self.editCustomerButton.setText(_translate("EditCustomerWidget", "Edit Customer"))
        self.groupBox.setTitle(_translate("EditCustomerWidget", "Edit Customer"))
        self.label.setText(_translate("EditCustomerWidget", "Account Name"))
        self.editCustomerAccountSelectionBox.setItemText(0, _translate("EditCustomerWidget", "Select..."))
        self.editCustomerAccountSelectionBox.setItemText(1, _translate("EditCustomerWidget", "BC Tree Fruit Inc."))
        self.editCustomerAccountSelectionBox.setItemText(2, _translate("EditCustomerWidget", "SunRype Inc."))
        self.editCustomerAccountSelectionBox.setItemText(3, _translate("EditCustomerWidget", "Tantalus Winery Inc."))
        self.label_3.setText(_translate("EditCustomerWidget", "Account ID"))
        self.editCustomerId.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_2.setText(_translate("EditCustomerWidget", "Street Address"))
        self.editCustomerStreetAddressLine1.setToolTip(_translate("EditCustomerWidget", "Street Address"))
        self.editCustomerStreetAddressLine1.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_4.setText(_translate("EditCustomerWidget", "Street Address Line 2"))
        self.editCustomerStreetAddressLine2.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_5.setText(_translate("EditCustomerWidget", "City"))
        self.editCustomerCity.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_8.setText(_translate("EditCustomerWidget", "Region"))
        self.editCustomerRegion.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_7.setText(_translate("EditCustomerWidget", "Postal Code"))
        self.editCustomerPostalCode.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_10.setText(_translate("EditCustomerWidget", "Country"))
        self.editCustomerCountry.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_6.setText(_translate("EditCustomerWidget", "Phone Number"))
        self.editCustomerPhoneNumber.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))
        self.label_9.setText(_translate("EditCustomerWidget", "Email"))
        self.editCustomerEmail.setPlaceholderText(_translate("EditCustomerWidget", "Auto-fills from Account Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditCustomerWidget = QtWidgets.QWidget()
    ui = Ui_EditCustomerWidget()
    ui.setupUi(EditCustomerWidget)
    EditCustomerWidget.show()
    sys.exit(app.exec())