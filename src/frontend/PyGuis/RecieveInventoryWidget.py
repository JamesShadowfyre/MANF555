# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecieveInventoryWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recieveInventoryWidget(object):
    def setupUi(self, recieveInventoryWidget):
        recieveInventoryWidget.setObjectName("recieveInventoryWidget")
        recieveInventoryWidget.resize(487, 399)
        self.recieveInventorySaveButton = QtWidgets.QPushButton(recieveInventoryWidget)
        self.recieveInventorySaveButton.setGeometry(QtCore.QRect(180, 340, 93, 28))
        self.recieveInventorySaveButton.setObjectName("recieveInventorySaveButton")
        self.groupBox = QtWidgets.QGroupBox(recieveInventoryWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 441, 231))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 411, 182))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.recieveInvItemID = QtWidgets.QComboBox(self.formLayoutWidget)
        self.recieveInvItemID.setObjectName("recieveInvItemID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.recieveInvItemID)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.recieveInvDescription = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.recieveInvDescription.setObjectName("recieveInvDescription")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.recieveInvDescription)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.recieveInvCost = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.recieveInvCost.setObjectName("recieveInvCost")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.recieveInvCost)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.recieveInvQty = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.recieveInvQty.setObjectName("recieveInvQty")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.recieveInvQty)
        self.recieveInvItemName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.recieveInvItemName.setObjectName("recieveInvItemName")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.recieveInvItemName)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.recieveInvInternalPartID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.recieveInvInternalPartID.setObjectName("recieveInvInternalPartID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.recieveInvInternalPartID)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.recieveInventoryNoteBox = QtWidgets.QGroupBox(recieveInventoryWidget)
        self.recieveInventoryNoteBox.setGeometry(QtCore.QRect(10, 250, 441, 80))
        self.recieveInventoryNoteBox.setObjectName("recieveInventoryNoteBox")
        self.label_7 = QtWidgets.QLabel(self.recieveInventoryNoteBox)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 381, 21))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(recieveInventoryWidget)
        QtCore.QMetaObject.connectSlotsByName(recieveInventoryWidget)

    def retranslateUi(self, recieveInventoryWidget):
        _translate = QtCore.QCoreApplication.translate
        recieveInventoryWidget.setWindowTitle(_translate("recieveInventoryWidget", "Recieve Inventory"))
        self.recieveInventorySaveButton.setText(_translate("recieveInventoryWidget", "Save"))
        self.groupBox.setTitle(_translate("recieveInventoryWidget", "Recieve Inventory"))
        self.label_3.setText(_translate("recieveInventoryWidget", "Item Name"))
        self.label_5.setText(_translate("recieveInventoryWidget", "Item Description"))
   
        self.label_6.setText(_translate("recieveInventoryWidget", "Item Cost"))

        self.label_4.setText(_translate("recieveInventoryWidget", "Quantity Received"))
        self.label_11.setText(_translate("recieveInventoryWidget", "Internal Part ID"))

        self.label_2.setText(_translate("recieveInventoryWidget", "Item ID"))
        self.recieveInventoryNoteBox.setTitle(_translate("recieveInventoryWidget", "Notes:"))
        self.label_7.setText(_translate("recieveInventoryWidget", "Use this module while receiving new inventory."))
