# Form implementation generated from reading ui file 'EditOperatorWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_editOperatorWidget(object):
    def setupUi(self, editOperatorWidget):
        editOperatorWidget.setObjectName("editOperatorWidget")
        editOperatorWidget.resize(438, 168)
        self.groupBox = QtWidgets.QGroupBox(parent=editOperatorWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 101))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.newEmployeeNumberInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.newEmployeeNumberInput.setObjectName("newEmployeeNumberInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newEmployeeNumberInput)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.newOperatorNameInput = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.newOperatorNameInput.setObjectName("newOperatorNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newOperatorNameInput)
        self.saveOperatorButton = QtWidgets.QPushButton(parent=editOperatorWidget)
        self.saveOperatorButton.setGeometry(QtCore.QRect(130, 120, 131, 24))
        self.saveOperatorButton.setObjectName("saveOperatorButton")

        self.retranslateUi(editOperatorWidget)
        QtCore.QMetaObject.connectSlotsByName(editOperatorWidget)

    def retranslateUi(self, editOperatorWidget):
        _translate = QtCore.QCoreApplication.translate
        editOperatorWidget.setWindowTitle(_translate("editOperatorWidget", "Edit Operator"))
        self.groupBox.setTitle(_translate("editOperatorWidget", "Edit Operator"))
        self.label.setText(_translate("editOperatorWidget", "Operator Name"))
        self.label_2.setText(_translate("editOperatorWidget", "Employee Number"))
        self.saveOperatorButton.setText(_translate("editOperatorWidget", "Save Changes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editOperatorWidget = QtWidgets.QWidget()
    ui = Ui_editOperatorWidget()
    ui.setupUi(editOperatorWidget)
    editOperatorWidget.show()
    sys.exit(app.exec())