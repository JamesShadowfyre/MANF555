# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editCustomerWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_removeCustomerWidget(object):
    def setupUi(self, removeCustomerWidget):
        removeCustomerWidget.setObjectName("removeCustomerWidget")
        removeCustomerWidget.resize(500, 331)
        self.deleteCustomerButton = QtWidgets.QPushButton(removeCustomerWidget)
        self.deleteCustomerButton.setGeometry(QtCore.QRect(180, 310, 141, 24))
        self.deleteCustomerButton.setObjectName("deleteCustomerButton")
        self.groupBox = QtWidgets.QGroupBox(removeCustomerWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 481, 281))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 461, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.accountInformationLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.accountInformationLayout.setContentsMargins(0, 0, 0, 0)
        self.accountInformationLayout.setObjectName("accountInformationLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.accountInformationLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.accountInformationLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.accountInformationLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.removeCustomerId = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerId.setPlaceholderText("")
        self.removeCustomerId.setObjectName("removeCustomerId")
        self.accountInformationLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.removeCustomerId)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.accountInformationLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.removeCustomerStreetAddressLine1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerStreetAddressLine1.setPlaceholderText("")
        self.removeCustomerStreetAddressLine1.setObjectName("removeCustomerStreetAddressLine1")
        self.accountInformationLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.removeCustomerStreetAddressLine1)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.accountInformationLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.removeCustomerStreetAddressLine2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerStreetAddressLine2.setPlaceholderText("")
        self.removeCustomerStreetAddressLine2.setObjectName("removeCustomerStreetAddressLine2")
        self.accountInformationLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.removeCustomerStreetAddressLine2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.accountInformationLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.removeCustomerCity = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerCity.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.removeCustomerCity.setPlaceholderText("")
        self.removeCustomerCity.setObjectName("removeCustomerCity")
        self.accountInformationLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.removeCustomerCity)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.accountInformationLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.accountInformationLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.removeCustomerPostalCode = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerPostalCode.setPlaceholderText("")
        self.removeCustomerPostalCode.setObjectName("removeCustomerPostalCode")
        self.accountInformationLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.removeCustomerPostalCode)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.accountInformationLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.accountInformationLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.removeCustomerPhoneNumber = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerPhoneNumber.setPlaceholderText("")
        self.removeCustomerPhoneNumber.setObjectName("removeCustomerPhoneNumber")
        self.accountInformationLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.removeCustomerPhoneNumber)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.accountInformationLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.removeCustomerEmail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.removeCustomerEmail.setPlaceholderText("")
        self.removeCustomerEmail.setObjectName("removeCustomerEmail")
        self.accountInformationLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.removeCustomerEmail)
        self.billingRegionInput_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.billingRegionInput_2.setObjectName("billingRegionInput_2")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.setItemText(0, "")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.billingRegionInput_2.addItem("")
        self.accountInformationLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.billingRegionInput_2)
        self.billingCountryInput_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.billingCountryInput_2.setObjectName("billingCountryInput_2")
        self.billingCountryInput_2.addItem("")
        self.billingCountryInput_2.addItem("")
        self.billingCountryInput_2.addItem("")
        self.accountInformationLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.billingCountryInput_2)

        self.retranslateUi(removeCustomerWidget)
        QtCore.QMetaObject.connectSlotsByName(removeCustomerWidget)

    def retranslateUi(self, removeCustomerWidget):
        _translate = QtCore.QCoreApplication.translate
        removeCustomerWidget.setWindowTitle(_translate("removeCustomerWidget", "Edit Customer"))
        self.deleteCustomerButton.setText(_translate("removeCustomerWidget", "Save Changes"))
        self.groupBox.setTitle(_translate("removeCustomerWidget", "Edit Customer"))
        self.label.setText(_translate("removeCustomerWidget", "Account Name"))
        self.comboBox_2.setItemText(0, _translate("removeCustomerWidget", "Select..."))
        self.comboBox_2.setItemText(1, _translate("removeCustomerWidget", "BC Tree Fruit Inc."))
        self.comboBox_2.setItemText(2, _translate("removeCustomerWidget", "SunRype Inc."))
        self.comboBox_2.setItemText(3, _translate("removeCustomerWidget", "Tantalus Winery Inc."))
        self.label_3.setText(_translate("removeCustomerWidget", "Account ID"))
        self.label_2.setText(_translate("removeCustomerWidget", "Street Address"))
        self.removeCustomerStreetAddressLine1.setToolTip(_translate("removeCustomerWidget", "Street Address"))
        self.label_4.setText(_translate("removeCustomerWidget", "Street Address Line 2"))
        self.label_5.setText(_translate("removeCustomerWidget", "City"))
        self.label_8.setText(_translate("removeCustomerWidget", "Region"))
        self.label_7.setText(_translate("removeCustomerWidget", "Postal Code"))
        self.label_10.setText(_translate("removeCustomerWidget", "Country"))
        self.label_6.setText(_translate("removeCustomerWidget", "Phone Number"))
        self.label_9.setText(_translate("removeCustomerWidget", "Email"))
        self.billingRegionInput_2.setToolTip(_translate("removeCustomerWidget", "Province"))
        self.billingRegionInput_2.setItemText(1, _translate("removeCustomerWidget", "AB"))
        self.billingRegionInput_2.setItemText(2, _translate("removeCustomerWidget", "BC"))
        self.billingRegionInput_2.setItemText(3, _translate("removeCustomerWidget", "MB"))
        self.billingRegionInput_2.setItemText(4, _translate("removeCustomerWidget", "NB"))
        self.billingRegionInput_2.setItemText(5, _translate("removeCustomerWidget", "NL"))
        self.billingRegionInput_2.setItemText(6, _translate("removeCustomerWidget", "NS"))
        self.billingRegionInput_2.setItemText(7, _translate("removeCustomerWidget", "NT"))
        self.billingRegionInput_2.setItemText(8, _translate("removeCustomerWidget", "NU"))
        self.billingRegionInput_2.setItemText(9, _translate("removeCustomerWidget", "ON"))
        self.billingRegionInput_2.setItemText(10, _translate("removeCustomerWidget", "PE"))
        self.billingRegionInput_2.setItemText(11, _translate("removeCustomerWidget", "QC"))
        self.billingRegionInput_2.setItemText(12, _translate("removeCustomerWidget", "SK"))
        self.billingRegionInput_2.setItemText(13, _translate("removeCustomerWidget", "YT"))
        self.billingCountryInput_2.setItemText(0, _translate("removeCustomerWidget", "-"))
        self.billingCountryInput_2.setItemText(1, _translate("removeCustomerWidget", "Canada"))
        self.billingCountryInput_2.setItemText(2, _translate("removeCustomerWidget", "Other"))
