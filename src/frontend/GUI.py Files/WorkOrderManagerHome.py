# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkOrderManagerHome.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkOrderManagerWidget(object):
    def setupUi(self, WorkOrderManagerWidget):
        WorkOrderManagerWidget.setObjectName("WorkOrderManagerWidget")
        WorkOrderManagerWidget.resize(1070, 379)
        self.groupBox_2 = QtWidgets.QGroupBox(WorkOrderManagerWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 110, 1071, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 1051, 191))
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
        self.groupBox = QtWidgets.QGroupBox(WorkOrderManagerWidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 831, 81))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 791, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.createWOButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.createWOButton.setObjectName("createWOButton")
        self.horizontalLayout.addWidget(self.createWOButton)
        self.editWOButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editWOButton.setObjectName("editWOButton")
        self.horizontalLayout.addWidget(self.editWOButton)
        self.deleteWOButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteWOButton.setObjectName("deleteWOButton")
        self.horizontalLayout.addWidget(self.deleteWOButton)
        self.completedWOButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.completedWOButton.setObjectName("completedWOButton")
        self.horizontalLayout.addWidget(self.completedWOButton)
        self.customerManagerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.customerManagerButton.setObjectName("customerManagerButton")
        self.horizontalLayout.addWidget(self.customerManagerButton)
        self.actionEdit = QtWidgets.QAction(WorkOrderManagerWidget)
        self.actionEdit.setObjectName("actionEdit")

        self.retranslateUi(WorkOrderManagerWidget)
        QtCore.QMetaObject.connectSlotsByName(WorkOrderManagerWidget)

    def retranslateUi(self, WorkOrderManagerWidget):
        _translate = QtCore.QCoreApplication.translate
        WorkOrderManagerWidget.setWindowTitle(_translate("WorkOrderManagerWidget", "Work Order Manager"))
        self.groupBox_2.setTitle(_translate("WorkOrderManagerWidget", "All Work Orders"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("WorkOrderManagerWidget", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("WorkOrderManagerWidget", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("WorkOrderManagerWidget", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("WorkOrderManagerWidget", "4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("WorkOrderManagerWidget", "Work Order No."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("WorkOrderManagerWidget", "Date Recieved"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("WorkOrderManagerWidget", "Date Finished"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("WorkOrderManagerWidget", "Account ID"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("WorkOrderManagerWidget", "Drilling Arrangement"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("WorkOrderManagerWidget", "Qty"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("WorkOrderManagerWidget", "Operator"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("WorkOrderManagerWidget", "0098"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-15-2024"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-15-2024"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("WorkOrderManagerWidget", "ACCT_0040"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("WorkOrderManagerWidget", "2L"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("WorkOrderManagerWidget", "322"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("WorkOrderManagerWidget", "mDavies"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("WorkOrderManagerWidget", "0099"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-15-2024"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-18-2024"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("WorkOrderManagerWidget", "ACCT_0984"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("WorkOrderManagerWidget", "2R"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("WorkOrderManagerWidget", "16"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("WorkOrderManagerWidget", "jRopotar"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("WorkOrderManagerWidget", "0100"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-15-2024"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-16-2024"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("WorkOrderManagerWidget", "ACCT_0732"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("WorkOrderManagerWidget", "0"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("WorkOrderManagerWidget", "88"))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("WorkOrderManagerWidget", "jKettle"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("WorkOrderManagerWidget", "0101"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-16-2024"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("WorkOrderManagerWidget", "Nov-17-2024"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("WorkOrderManagerWidget", "ACCT_0869"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("WorkOrderManagerWidget", "ALL"))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("WorkOrderManagerWidget", "192"))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("WorkOrderManagerWidget", "mDavies"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("WorkOrderManagerWidget", "Work Order Manager"))
        self.createWOButton.setText(_translate("WorkOrderManagerWidget", "Create Work Order"))
        self.editWOButton.setText(_translate("WorkOrderManagerWidget", "Edit Work Order"))
        self.deleteWOButton.setText(_translate("WorkOrderManagerWidget", "Delete Work Order"))
        self.completedWOButton.setText(_translate("WorkOrderManagerWidget", "Completed Work Orders"))
        self.customerManagerButton.setText(_translate("WorkOrderManagerWidget", "Customer Manager"))
        self.actionEdit.setText(_translate("WorkOrderManagerWidget", "Edit"))
