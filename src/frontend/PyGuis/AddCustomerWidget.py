# Form implementation generated from reading ui file 'AddCustomerWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddNewCustomerWidget(object):
    def setupUi(self, AddNewCustomerWidget):
        AddNewCustomerWidget.setObjectName("AddNewCustomerWidget")
        AddNewCustomerWidget.resize(1089, 535)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddNewCustomerWidget.sizePolicy().hasHeightForWidth())
        AddNewCustomerWidget.setSizePolicy(sizePolicy)
        self.label_3 = QtWidgets.QLabel(parent=AddNewCustomerWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 401, 19))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=AddNewCustomerWidget)
        self.pushButton.setGeometry(QtCore.QRect(980, 460, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(parent=AddNewCustomerWidget)
        self.groupBox.setGeometry(QtCore.QRect(560, 50, 531, 331))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 511, 291))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.billingInformationLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.billingInformationLayout.setContentsMargins(0, 0, 0, 0)
        self.billingInformationLayout.setObjectName("billingInformationLayout")
        self.label_12 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.billingInformationLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.billingNameInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingNameInput.setObjectName("billingNameInput")
        self.billingInformationLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingNameInput)
        self.label_13 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.billingInformationLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.billingStreetAddressLine1Input = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingStreetAddressLine1Input.setText("")
        self.billingStreetAddressLine1Input.setObjectName("billingStreetAddressLine1Input")
        self.billingInformationLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingStreetAddressLine1Input)
        self.label_14 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.billingInformationLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.billingStreetAddressLine2Input = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingStreetAddressLine2Input.setObjectName("billingStreetAddressLine2Input")
        self.billingInformationLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingStreetAddressLine2Input)
        self.label_15 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.billingInformationLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.billingCityInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingCityInput.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.billingCityInput.setObjectName("billingCityInput")
        self.billingInformationLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingCityInput)
        self.label_16 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.billingInformationLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.billingRegionInput = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.billingRegionInput.setObjectName("billingRegionInput")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.setItemText(0, "")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingRegionInput.addItem("")
        self.billingInformationLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingRegionInput)
        self.label_17 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.billingInformationLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.billingPostalCodeInput_2 = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingPostalCodeInput_2.setObjectName("billingPostalCodeInput_2")
        self.billingInformationLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingPostalCodeInput_2)
        self.label_20 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.billingInformationLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_20)
        self.billingCountryInput = QtWidgets.QComboBox(parent=self.formLayoutWidget_2)
        self.billingCountryInput.setObjectName("billingCountryInput")
        self.billingCountryInput.addItem("")
        self.billingCountryInput.addItem("")
        self.billingCountryInput.addItem("")
        self.billingInformationLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingCountryInput)
        self.label_18 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.billingInformationLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_18)
        self.billingPhoneNumberInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingPhoneNumberInput.setObjectName("billingPhoneNumberInput")
        self.billingInformationLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingPhoneNumberInput)
        self.label_19 = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.billingInformationLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_19)
        self.billingEmailInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget_2)
        self.billingEmailInput.setObjectName("billingEmailInput")
        self.billingInformationLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.billingEmailInput)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=AddNewCustomerWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 430, 531, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 511, 51))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_21 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=AddNewCustomerWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 50, 531, 361))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 511, 311))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.accountInformationLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.accountInformationLayout.setContentsMargins(0, 0, 0, 0)
        self.accountInformationLayout.setObjectName("accountInformationLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.accountInformationLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.accountNameInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.accountNameInput.setObjectName("accountNameInput")
        self.accountInformationLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.accountNameInput)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.accountInformationLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.streetAddressLine1Input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.streetAddressLine1Input.setObjectName("streetAddressLine1Input")
        self.accountInformationLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.streetAddressLine1Input)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.accountInformationLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.streetAddressLine2Input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.streetAddressLine2Input.setObjectName("streetAddressLine2Input")
        self.accountInformationLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.streetAddressLine2Input)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.accountInformationLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.accountInformationLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_4)
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.accountInformationLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.regionInput = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.regionInput.setObjectName("regionInput")
        self.regionInput.addItem("")
        self.regionInput.setItemText(0, "")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.regionInput.addItem("")
        self.accountInformationLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.regionInput)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.accountInformationLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.postalCodeInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.postalCodeInput.setObjectName("postalCodeInput")
        self.accountInformationLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.postalCodeInput)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.accountInformationLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.comboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.accountInformationLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.accountInformationLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.phoneNumberInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.phoneNumberInput.setObjectName("phoneNumberInput")
        self.accountInformationLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.phoneNumberInput)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.accountInformationLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.emailInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.emailInput.setObjectName("emailInput")
        self.accountInformationLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.emailInput)
        self.label_11 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.accountInformationLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.checkBox = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.accountInformationLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox)

        self.retranslateUi(AddNewCustomerWidget)
        QtCore.QMetaObject.connectSlotsByName(AddNewCustomerWidget)

    def retranslateUi(self, AddNewCustomerWidget):
        _translate = QtCore.QCoreApplication.translate
        AddNewCustomerWidget.setWindowTitle(_translate("AddNewCustomerWidget", "Add Customer"))
        self.label_3.setText(_translate("AddNewCustomerWidget", "Please fill out the customer information form below:"))
        self.pushButton.setText(_translate("AddNewCustomerWidget", "Save"))
        self.groupBox.setTitle(_translate("AddNewCustomerWidget", "Billing Information"))
        self.label_12.setText(_translate("AddNewCustomerWidget", "Account Name"))
        self.label_13.setText(_translate("AddNewCustomerWidget", "Street Address"))
        self.billingStreetAddressLine1Input.setToolTip(_translate("AddNewCustomerWidget", "Street Address"))
        self.billingStreetAddressLine1Input.setPlaceholderText(_translate("AddNewCustomerWidget", "Street Address"))
        self.label_14.setText(_translate("AddNewCustomerWidget", "Street Address Line 2"))
        self.billingStreetAddressLine2Input.setPlaceholderText(_translate("AddNewCustomerWidget", "Street Address Line 2"))
        self.label_15.setText(_translate("AddNewCustomerWidget", "City"))
        self.billingCityInput.setPlaceholderText(_translate("AddNewCustomerWidget", "City"))
        self.label_16.setText(_translate("AddNewCustomerWidget", "Region"))
        self.billingRegionInput.setToolTip(_translate("AddNewCustomerWidget", "Province"))
        self.billingRegionInput.setItemText(1, _translate("AddNewCustomerWidget", "AB"))
        self.billingRegionInput.setItemText(2, _translate("AddNewCustomerWidget", "BC"))
        self.billingRegionInput.setItemText(3, _translate("AddNewCustomerWidget", "MB"))
        self.billingRegionInput.setItemText(4, _translate("AddNewCustomerWidget", "NB"))
        self.billingRegionInput.setItemText(5, _translate("AddNewCustomerWidget", "NL"))
        self.billingRegionInput.setItemText(6, _translate("AddNewCustomerWidget", "NS"))
        self.billingRegionInput.setItemText(7, _translate("AddNewCustomerWidget", "NT"))
        self.billingRegionInput.setItemText(8, _translate("AddNewCustomerWidget", "NU"))
        self.billingRegionInput.setItemText(9, _translate("AddNewCustomerWidget", "ON"))
        self.billingRegionInput.setItemText(10, _translate("AddNewCustomerWidget", "PE"))
        self.billingRegionInput.setItemText(11, _translate("AddNewCustomerWidget", "QC"))
        self.billingRegionInput.setItemText(12, _translate("AddNewCustomerWidget", "SK"))
        self.billingRegionInput.setItemText(13, _translate("AddNewCustomerWidget", "YT"))
        self.label_17.setText(_translate("AddNewCustomerWidget", "Postal Code"))
        self.billingPostalCodeInput_2.setPlaceholderText(_translate("AddNewCustomerWidget", "Postal Code"))
        self.label_20.setText(_translate("AddNewCustomerWidget", "Country"))
        self.billingCountryInput.setItemText(0, _translate("AddNewCustomerWidget", "-"))
        self.billingCountryInput.setItemText(1, _translate("AddNewCustomerWidget", "Canada"))
        self.billingCountryInput.setItemText(2, _translate("AddNewCustomerWidget", "Other"))
        self.label_18.setText(_translate("AddNewCustomerWidget", "Phone Number"))
        self.billingPhoneNumberInput.setPlaceholderText(_translate("AddNewCustomerWidget", "Phone Number"))
        self.label_19.setText(_translate("AddNewCustomerWidget", "Email"))
        self.billingEmailInput.setPlaceholderText(_translate("AddNewCustomerWidget", "Email Address"))
        self.groupBox_2.setTitle(_translate("AddNewCustomerWidget", "Payment"))
        self.label_21.setText(_translate("AddNewCustomerWidget", "Preferred Payment Type"))
        self.comboBox_2.setItemText(0, _translate("AddNewCustomerWidget", "-"))
        self.comboBox_2.setItemText(1, _translate("AddNewCustomerWidget", "Cheque"))
        self.comboBox_2.setItemText(2, _translate("AddNewCustomerWidget", "EFT"))
        self.comboBox_2.setItemText(3, _translate("AddNewCustomerWidget", "Credit Card"))
        self.groupBox_3.setTitle(_translate("AddNewCustomerWidget", "Account Information"))
        self.label.setText(_translate("AddNewCustomerWidget", "Account Name"))
        self.accountNameInput.setPlaceholderText(_translate("AddNewCustomerWidget", "Account Name"))
        self.label_2.setText(_translate("AddNewCustomerWidget", "Street Address"))
        self.streetAddressLine1Input.setToolTip(_translate("AddNewCustomerWidget", "Street Address"))
        self.streetAddressLine1Input.setPlaceholderText(_translate("AddNewCustomerWidget", "Street Address"))
        self.label_4.setText(_translate("AddNewCustomerWidget", "Street Address Line 2"))
        self.streetAddressLine2Input.setPlaceholderText(_translate("AddNewCustomerWidget", "Street Address Line 2"))
        self.label_5.setText(_translate("AddNewCustomerWidget", "City"))
        self.lineEdit_4.setPlaceholderText(_translate("AddNewCustomerWidget", "City"))
        self.label_8.setText(_translate("AddNewCustomerWidget", "Region"))
        self.regionInput.setToolTip(_translate("AddNewCustomerWidget", "Province"))
        self.regionInput.setItemText(1, _translate("AddNewCustomerWidget", "AB"))
        self.regionInput.setItemText(2, _translate("AddNewCustomerWidget", "BC"))
        self.regionInput.setItemText(3, _translate("AddNewCustomerWidget", "MB"))
        self.regionInput.setItemText(4, _translate("AddNewCustomerWidget", "NB"))
        self.regionInput.setItemText(5, _translate("AddNewCustomerWidget", "NL"))
        self.regionInput.setItemText(6, _translate("AddNewCustomerWidget", "NS"))
        self.regionInput.setItemText(7, _translate("AddNewCustomerWidget", "NT"))
        self.regionInput.setItemText(8, _translate("AddNewCustomerWidget", "NU"))
        self.regionInput.setItemText(9, _translate("AddNewCustomerWidget", "ON"))
        self.regionInput.setItemText(10, _translate("AddNewCustomerWidget", "PE"))
        self.regionInput.setItemText(11, _translate("AddNewCustomerWidget", "QC"))
        self.regionInput.setItemText(12, _translate("AddNewCustomerWidget", "SK"))
        self.regionInput.setItemText(13, _translate("AddNewCustomerWidget", "YT"))
        self.label_7.setText(_translate("AddNewCustomerWidget", "Postal Code"))
        self.postalCodeInput.setPlaceholderText(_translate("AddNewCustomerWidget", "Postal Code"))
        self.label_10.setText(_translate("AddNewCustomerWidget", "Country"))
        self.comboBox.setItemText(0, _translate("AddNewCustomerWidget", "-"))
        self.comboBox.setItemText(1, _translate("AddNewCustomerWidget", "Canada"))
        self.comboBox.setItemText(2, _translate("AddNewCustomerWidget", "Other"))
        self.label_6.setText(_translate("AddNewCustomerWidget", "Phone Number"))
        self.phoneNumberInput.setPlaceholderText(_translate("AddNewCustomerWidget", "Phone Number"))
        self.label_9.setText(_translate("AddNewCustomerWidget", "Email"))
        self.emailInput.setPlaceholderText(_translate("AddNewCustomerWidget", "Email Address"))
        self.label_11.setText(_translate("AddNewCustomerWidget", "Billing Information"))
        self.checkBox.setText(_translate("AddNewCustomerWidget", "Same as Account Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewCustomerWidget = QtWidgets.QWidget()
    ui = Ui_AddNewCustomerWidget()
    ui.setupUi(AddNewCustomerWidget)
    AddNewCustomerWidget.show()
    sys.exit(app.exec())