# Form implementation generated from reading ui file 'InventoryManager.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InventoryManager(object):
    def setupUi(self, InventoryManager):
        InventoryManager.setObjectName("InventoryManager")
        InventoryManager.resize(1091, 534)
        self.groupBox = QtWidgets.QGroupBox(parent=InventoryManager)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 291, 201))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 271, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=InventoryManager)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 10, 691, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 671, 181))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
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
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=InventoryManager)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 260, 691, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.groupBox_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 20, 671, 181))
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(125)

        self.retranslateUi(InventoryManager)
        QtCore.QMetaObject.connectSlotsByName(InventoryManager)

    def retranslateUi(self, InventoryManager):
        _translate = QtCore.QCoreApplication.translate
        InventoryManager.setWindowTitle(_translate("InventoryManager", "Inventory Manager"))
        self.groupBox.setTitle(_translate("InventoryManager", "Inventory Manager"))
        self.pushButton.setText(_translate("InventoryManager", "Add Inventory"))
        self.pushButton_4.setText(_translate("InventoryManager", "Perform Inventory Cycle Count"))
        self.pushButton_3.setText(_translate("InventoryManager", "Create New Inventory Item"))
        self.pushButton_2.setText(_translate("InventoryManager", "Low Inventory Alarm Settings"))
        self.groupBox_2.setTitle(_translate("InventoryManager", "Inventory List"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("InventoryManager", "Item"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("InventoryManager", "Part ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("InventoryManager", "Qty OnHand"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("InventoryManager", "Part Description"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("InventoryManager", "Colour"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("InventoryManager", "Part Cost"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("InventoryManager", "0001"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("InventoryManager", "4"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("InventoryManager", "Back Case"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("InventoryManager", "Black"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("InventoryManager", "10"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("InventoryManager", "Low Inventory List"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("InventoryManager", "Item"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("InventoryManager", "Part ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("InventoryManager", "Qty OnHand"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("InventoryManager", "Part Description"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("InventoryManager", "Colour"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("InventoryManager", "Part Cost"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("InventoryManager", "0001"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("InventoryManager", "4"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("InventoryManager", "Back Case"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("InventoryManager", "Black"))
        item = self.tableWidget_2.item(0, 4)
        item.setText(_translate("InventoryManager", "10"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InventoryManager = QtWidgets.QWidget()
    ui = Ui_InventoryManager()
    ui.setupUi(InventoryManager)
    InventoryManager.show()
    sys.exit(app.exec())