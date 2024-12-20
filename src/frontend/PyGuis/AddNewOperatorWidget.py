# Form implementation generated from reading ui file 'AddNewOperatorWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets as qtw


class Ui_addNewOperatorWidget(object):
    def setupUi(self, addNewOperatorWidget: qtw.QWidget):
        addNewOperatorWidget.setObjectName("addNewOperatorWidget")
        addNewOperatorWidget.resize(433, 169)
        addNewOperatorWidget.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")

        self.groupBox = QtWidgets.QGroupBox(addNewOperatorWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 150))
        self.groupBox.setObjectName("groupBox")

        self.saveOperatorButton = QtWidgets.QPushButton(self.groupBox)
        self.saveOperatorButton.setGeometry(QtCore.QRect(130, 120, 131, 24))
        self.saveOperatorButton.setObjectName("saveOperatorButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.newEmployeeNumberInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.newEmployeeNumberInput.setObjectName("newEmployeeNumberInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newEmployeeNumberInput)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.newOperatorNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.newOperatorNameInput.setObjectName("newOperatorNameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.newOperatorNameInput)

        self.retranslateUi(addNewOperatorWidget)
        QtCore.QMetaObject.connectSlotsByName(addNewOperatorWidget)


    
    def retranslateUi(self, addNewOperatorWidget):
        _translate = QtCore.QCoreApplication.translate
        addNewOperatorWidget.setWindowTitle(_translate("addNewOperatorWidget", "Add New Operator"))
        self.saveOperatorButton.setText(_translate("addNewOperatorWidget", "Save Operator"))
        self.groupBox.setTitle(_translate("addNewOperatorWidget", "Add New Operator"))
        self.label.setText(_translate("addNewOperatorWidget", "Operator Name"))
        self.label_2.setText(_translate("addNewOperatorWidget", "Employee Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addNewOperatorWidget = QtWidgets.QWidget()
    ui = Ui_addNewOperatorWidget()
    ui.setupUi(addNewOperatorWidget)
    addNewOperatorWidget.show()
    sys.exit(app.exec())
