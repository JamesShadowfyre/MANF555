from EditOperatorWidget import Ui_editOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class EditOperatorWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_editOperatorWidget()
        self.ui.setupUi(self)
        self.ui.saveOperatorButton.clicked.connect(self.saveOperatorButtonClicked)
 # Set QIntValidator to restrict input to integers only
        self.ui.newEmployeeNumberInput.setValidator(QIntValidator())  # Accept any integer value

    def saveOperatorButtonClicked(self):
        operatorName =  self.ui.newOperatorNameInput.text()
        employeeNumber = self.ui.newEmployeeNumberInput.text()

        print("New Operator Name: ")
        print(operatorName)
        print("New Employee Number: ")
        print(employeeNumber)
        self.close()
        pass

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditOperatorWidgetHandler()
    widget.show()
    app.exec()