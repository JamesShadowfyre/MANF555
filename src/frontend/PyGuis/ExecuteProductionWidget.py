# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExecuteProductionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExecuteProduction(object):
    def setupUi(self, ExecuteProduction):
        ExecuteProduction.setObjectName("ExecuteProduction")
        ExecuteProduction.resize(640, 572)
        self.executeProductionButton = QtWidgets.QPushButton(ExecuteProduction)
        self.executeProductionButton.setGeometry(QtCore.QRect(410, 540, 75, 24))
        self.executeProductionButton.setObjectName("executeProductionButton")
        self.groupBox_3 = QtWidgets.QGroupBox(ExecuteProduction)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 621, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 601, 191))
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(145)
        self.createNewWOBox = QtWidgets.QGroupBox(ExecuteProduction)
        self.createNewWOBox.setGeometry(QtCore.QRect(10, 260, 471, 271))
        self.createNewWOBox.setObjectName("createNewWOBox")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.createNewWOBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 461, 251))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.executeWOCustomerSelection = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.executeWOCustomerSelection.setObjectName("executeWOCustomerSelection")
        self.executeWOCustomerSelection.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.executeWOCustomerSelection)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.executeWODateInput = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.executeWODateInput.setObjectName("executeWODateInput")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.executeWODateInput)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.executeWOBackCaseDetailsInput = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.executeWOBackCaseDetailsInput.setObjectName("executeWOBackCaseDetailsInput")
        self.executeWOBackCaseDetailsInput.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.executeWOBackCaseDetailsInput)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.executeWODrillingArrangementSelection = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.executeWODrillingArrangementSelection.setObjectName("executeWODrillingArrangementSelection")
        self.executeWODrillingArrangementSelection.addItem("")
        self.executeWODrillingArrangementSelection.addItem("")
        self.executeWODrillingArrangementSelection.addItem("")
        self.executeWODrillingArrangementSelection.addItem("")
        self.executeWODrillingArrangementSelection.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.executeWODrillingArrangementSelection)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.executeWOQuantityInput = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.executeWOQuantityInput.setObjectName("executeWOQuantityInput")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.executeWOQuantityInput)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.executeWOProductionDateInput = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.executeWOProductionDateInput.setObjectName("executeWOProductionDateInput")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.executeWOProductionDateInput)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.executeWOShippingMethod = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.executeWOShippingMethod.setObjectName("executeWOShippingMethod")
        self.executeWOShippingMethod.addItem("")
        self.executeWOShippingMethod.setItemText(0, "")
        self.executeWOShippingMethod.addItem("")
        self.executeWOShippingMethod.addItem("")
        self.executeWOShippingMethod.addItem("")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.executeWOShippingMethod)
        self.executeWONumberComboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.executeWONumberComboBox.setObjectName("executeWONumberComboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.executeWONumberComboBox)

        self.retranslateUi(ExecuteProduction)
        QtCore.QMetaObject.connectSlotsByName(ExecuteProduction)

    def retranslateUi(self, ExecuteProduction):
        _translate = QtCore.QCoreApplication.translate
        ExecuteProduction.setWindowTitle(_translate("ExecuteProduction", "Execute"))
        self.executeProductionButton.setText(_translate("ExecuteProduction", "Execute"))
        self.groupBox_3.setTitle(_translate("ExecuteProduction", "Work Order Selection"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ExecuteProduction", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ExecuteProduction", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ExecuteProduction", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ExecuteProduction", "4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ExecuteProduction", "Work Order No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ExecuteProduction", "Date Recieved"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ExecuteProduction", "Date Finished"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ExecuteProduction", "Account ID"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ExecuteProduction", "Drilling Arrangement"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ExecuteProduction", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ExecuteProduction", "Operator"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("ExecuteProduction", "0098"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("ExecuteProduction", "Nov-15-2024"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("ExecuteProduction", "Nov-15-2024"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("ExecuteProduction", "ACCT_0040"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("ExecuteProduction", "2L"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("ExecuteProduction", "322"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("ExecuteProduction", "mDavies"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("ExecuteProduction", "0099"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("ExecuteProduction", "Nov-15-2024"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("ExecuteProduction", "Nov-18-2024"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("ExecuteProduction", "ACCT_0984"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("ExecuteProduction", "2R"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("ExecuteProduction", "16"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("ExecuteProduction", "jRopotar"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("ExecuteProduction", "0100"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("ExecuteProduction", "Nov-15-2024"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("ExecuteProduction", "Nov-16-2024"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("ExecuteProduction", "ACCT_0732"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("ExecuteProduction", "0"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("ExecuteProduction", "88"))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("ExecuteProduction", "jKettle"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("ExecuteProduction", "0101"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("ExecuteProduction", "Nov-16-2024"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("ExecuteProduction", "Nov-17-2024"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("ExecuteProduction", "ACCT_0869"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("ExecuteProduction", "ALL"))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("ExecuteProduction", "192"))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("ExecuteProduction", "mDavies"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.createNewWOBox.setTitle(_translate("ExecuteProduction", "Selection Confirmation"))
        self.label_6.setText(_translate("ExecuteProduction", "Work Order Number"))
        self.label.setText(_translate("ExecuteProduction", "Customer"))
        self.executeWOCustomerSelection.setItemText(0, _translate("ExecuteProduction", "Auto-fills from selection"))
        self.label_2.setText(_translate("ExecuteProduction", "Order Date"))
        self.label_3.setText(_translate("ExecuteProduction", "Back Case Details"))
        self.executeWOBackCaseDetailsInput.setItemText(0, _translate("ExecuteProduction", "Auto-fills from selection"))
        self.label_4.setText(_translate("ExecuteProduction", "Drilling Arrangement"))
        self.executeWODrillingArrangementSelection.setItemText(0, _translate("ExecuteProduction", "Auto-fills from selection"))
        self.executeWODrillingArrangementSelection.setItemText(1, _translate("ExecuteProduction", "0"))
        self.executeWODrillingArrangementSelection.setItemText(2, _translate("ExecuteProduction", "2L"))
        self.executeWODrillingArrangementSelection.setItemText(3, _translate("ExecuteProduction", "2R"))
        self.executeWODrillingArrangementSelection.setItemText(4, _translate("ExecuteProduction", "ALL"))
        self.label_5.setText(_translate("ExecuteProduction", "Quantity"))
        self.label_7.setText(_translate("ExecuteProduction", "Production Date"))
        self.label_8.setText(_translate("ExecuteProduction", "Shipping Method"))
        self.executeWOShippingMethod.setItemText(1, _translate("ExecuteProduction", "Delievery (Address on File)"))
        self.executeWOShippingMethod.setItemText(2, _translate("ExecuteProduction", "Delivery (Other)"))
        self.executeWOShippingMethod.setItemText(3, _translate("ExecuteProduction", "Customer Pickup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExecuteProduction = QtWidgets.QWidget()
    ui = Ui_ExecuteProduction()
    ui.setupUi(ExecuteProduction)
    ExecuteProduction.show()
    sys.exit(app.exec_())
