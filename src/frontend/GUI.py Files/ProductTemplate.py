# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductTemplateWidget(object):
    def setupUi(self, ProductTemplateWidget):
        ProductTemplateWidget.setObjectName("ProductTemplateWidget")
        ProductTemplateWidget.resize(509, 329)
        self.groupBox = QtWidgets.QGroupBox(ProductTemplateWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 271))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.checkBox_4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_4)
        self.backCaseComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.backCaseComboBox.setObjectName("backCaseComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.backCaseComboBox)
        self.checkBox_3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.checkBox_5 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_9)
        self.comboBox_6 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.checkBox_10 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.checkBox_10)
        self.comboBox_7 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBox_7)
        self.productTemplateSave = QtWidgets.QPushButton(ProductTemplateWidget)
        self.productTemplateSave.setGeometry(QtCore.QRect(210, 290, 75, 24))
        self.productTemplateSave.setObjectName("productTemplateSave")

        self.retranslateUi(ProductTemplateWidget)
        QtCore.QMetaObject.connectSlotsByName(ProductTemplateWidget)

    def retranslateUi(self, ProductTemplateWidget):
        _translate = QtCore.QCoreApplication.translate
        ProductTemplateWidget.setWindowTitle(_translate("ProductTemplateWidget", "Product Template"))
        self.groupBox.setTitle(_translate("ProductTemplateWidget", "Product Template"))
        self.checkBox_4.setText(_translate("ProductTemplateWidget", "Back Case:"))
        self.checkBox_3.setText(_translate("ProductTemplateWidget", "Quality Data Collection:"))
        self.checkBox_5.setText(_translate("ProductTemplateWidget", "Drilling:"))
        self.checkBox_6.setText(_translate("ProductTemplateWidget", "Pick-by-Light:"))
        self.checkBox_7.setText(_translate("ProductTemplateWidget", "Rear Shell Assembly:"))
        self.checkBox_8.setText(_translate("ProductTemplateWidget", "Pressing:"))
        self.checkBox_9.setText(_translate("ProductTemplateWidget", "Label"))
        self.checkBox_10.setText(_translate("ProductTemplateWidget", "Output"))
        self.productTemplateSave.setText(_translate("ProductTemplateWidget", "Save"))
