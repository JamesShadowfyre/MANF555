# Form implementation generated from reading ui file 'EditWorkOrderWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_editWOSaveButton(object):
    def setupUi(self, editWOSaveButton):
        editWOSaveButton.setObjectName("editWOSaveButton")
        editWOSaveButton.resize(504, 484)
        self.pushButton = QtWidgets.QPushButton(parent=editWOSaveButton)
        self.pushButton.setGeometry(QtCore.QRect(350, 440, 141, 24))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=editWOSaveButton)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 310, 231, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 212, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.editWODeliveryAoFRadioButton = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.editWODeliveryAoFRadioButton.setObjectName("editWODeliveryAoFRadioButton")
        self.verticalLayout_2.addWidget(self.editWODeliveryAoFRadioButton)
        self.editWODeliveryOtherRadioButton = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.editWODeliveryOtherRadioButton.setObjectName("editWODeliveryOtherRadioButton")
        self.verticalLayout_2.addWidget(self.editWODeliveryOtherRadioButton)
        self.editWODeliveryPickupRadioButton = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.editWODeliveryPickupRadioButton.setObjectName("editWODeliveryPickupRadioButton")
        self.verticalLayout_2.addWidget(self.editWODeliveryPickupRadioButton)
        self.editWOBox = QtWidgets.QGroupBox(parent=editWOSaveButton)
        self.editWOBox.setGeometry(QtCore.QRect(10, 10, 481, 281))
        self.editWOBox.setObjectName("editWOBox")
        self.formLayoutWidget_3 = QtWidgets.QWidget(parent=self.editWOBox)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 461, 251))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.editWorkOrderNumberField_2 = QtWidgets.QTextBrowser(parent=self.formLayoutWidget_3)
        self.editWorkOrderNumberField_2.setMaximumSize(QtCore.QSize(1000, 25))
        self.editWorkOrderNumberField_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.editWorkOrderNumberField_2.setObjectName("editWorkOrderNumberField_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editWorkOrderNumberField_2)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.editWOCustomerSelection_2 = QtWidgets.QComboBox(parent=self.formLayoutWidget_3)
        self.editWOCustomerSelection_2.setObjectName("editWOCustomerSelection_2")
        self.editWOCustomerSelection_2.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editWOCustomerSelection_2)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.editWODateInput_2 = QtWidgets.QDateEdit(parent=self.formLayoutWidget_3)
        self.editWODateInput_2.setObjectName("editWODateInput_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editWODateInput_2)
        self.label_13 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.editWOQuantityInput_2 = QtWidgets.QSpinBox(parent=self.formLayoutWidget_3)
        self.editWOQuantityInput_2.setObjectName("editWOQuantityInput_2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editWOQuantityInput_2)
        self.label_14 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.editWOProductionDateInput_2 = QtWidgets.QDateEdit(parent=self.formLayoutWidget_3)
        self.editWOProductionDateInput_2.setObjectName("editWOProductionDateInput_2")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editWOProductionDateInput_2)
        self.requiredByDateLabel_2 = QtWidgets.QLabel(parent=self.formLayoutWidget_3)
        self.requiredByDateLabel_2.setObjectName("requiredByDateLabel_2")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.requiredByDateLabel_2)
        self.editWOrequiredByDate = QtWidgets.QDateEdit(parent=self.formLayoutWidget_3)
        self.editWOrequiredByDate.setObjectName("editWOrequiredByDate")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.editWOrequiredByDate)
        self.productTemplateViewButton_2 = QtWidgets.QPushButton(parent=editWOSaveButton)
        self.productTemplateViewButton_2.setGeometry(QtCore.QRect(350, 410, 141, 24))
        self.productTemplateViewButton_2.setObjectName("productTemplateViewButton_2")

        self.retranslateUi(editWOSaveButton)
        QtCore.QMetaObject.connectSlotsByName(editWOSaveButton)

    def retranslateUi(self, editWOSaveButton):
        _translate = QtCore.QCoreApplication.translate
        editWOSaveButton.setWindowTitle(_translate("editWOSaveButton", "Edit Work Order"))
        self.pushButton.setText(_translate("editWOSaveButton", "Save Changes"))
        self.groupBox_4.setTitle(_translate("editWOSaveButton", "Shipping Method"))
        self.editWODeliveryAoFRadioButton.setText(_translate("editWOSaveButton", "Delivery (Address on File)"))
        self.editWODeliveryOtherRadioButton.setText(_translate("editWOSaveButton", "Delivery (Other)"))
        self.editWODeliveryPickupRadioButton.setText(_translate("editWOSaveButton", "Customer Pickup"))
        self.editWOBox.setTitle(_translate("editWOSaveButton", "Edit Work Order"))
        self.label_8.setText(_translate("editWOSaveButton", "Work Order Number"))
        self.editWorkOrderNumberField_2.setHtml(_translate("editWOSaveButton", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("editWOSaveButton", "Customer"))
        self.editWOCustomerSelection_2.setItemText(0, _translate("editWOSaveButton", "Select..."))
        self.label_10.setText(_translate("editWOSaveButton", "Order Date"))
        self.label_13.setText(_translate("editWOSaveButton", "Quantity"))
        self.label_14.setText(_translate("editWOSaveButton", "Production Date"))
        self.requiredByDateLabel_2.setText(_translate("editWOSaveButton", "Required By: "))
        self.productTemplateViewButton_2.setText(_translate("editWOSaveButton", "Product Template"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editWOSaveButton = QtWidgets.QWidget()
    ui = Ui_editWOSaveButton()
    ui.setupUi(editWOSaveButton)
    editWOSaveButton.show()
    sys.exit(app.exec())
