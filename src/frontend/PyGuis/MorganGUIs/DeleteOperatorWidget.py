# Form implementation generated from reading ui file 'DeleteOperatorWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DeleteOperatorWidget(object):
    def setupUi(self, DeleteOperatorWidget):
        DeleteOperatorWidget.setObjectName("DeleteOperatorWidget")
        DeleteOperatorWidget.resize(430, 163)
        self.deleteOperatorButton = QtWidgets.QPushButton(parent=DeleteOperatorWidget)
        self.deleteOperatorButton.setGeometry(QtCore.QRect(120, 120, 171, 24))
        self.deleteOperatorButton.setObjectName("deleteOperatorButton")
        self.deleteOperatorBox = QtWidgets.QGroupBox(parent=DeleteOperatorWidget)
        self.deleteOperatorBox.setGeometry(QtCore.QRect(20, 10, 371, 101))
        self.deleteOperatorBox.setObjectName("deleteOperatorBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.deleteOperatorBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 351, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.deleteOperatorComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.deleteOperatorComboBox.setObjectName("deleteOperatorComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.deleteOperatorComboBox)
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.deleteEmployeeNumberBox = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.deleteEmployeeNumberBox.setObjectName("deleteEmployeeNumberBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.deleteEmployeeNumberBox)

        self.retranslateUi(DeleteOperatorWidget)
        QtCore.QMetaObject.connectSlotsByName(DeleteOperatorWidget)

    def retranslateUi(self, DeleteOperatorWidget):
        _translate = QtCore.QCoreApplication.translate
        DeleteOperatorWidget.setWindowTitle(_translate("DeleteOperatorWidget", "Delete Operator"))
        self.deleteOperatorButton.setText(_translate("DeleteOperatorWidget", "Delete Operator"))
        self.deleteOperatorBox.setTitle(_translate("DeleteOperatorWidget", "Delete Operator"))
        self.label.setText(_translate("DeleteOperatorWidget", "Operator Name"))
        self.label_2.setText(_translate("DeleteOperatorWidget", "Employee Number"))
        self.deleteEmployeeNumberBox.setPlaceholderText(_translate("DeleteOperatorWidget", "Autofills from Operator Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteOperatorWidget = QtWidgets.QWidget()
    ui = Ui_DeleteOperatorWidget()
    ui.setupUi(DeleteOperatorWidget)
    DeleteOperatorWidget.show()
    sys.exit(app.exec())
