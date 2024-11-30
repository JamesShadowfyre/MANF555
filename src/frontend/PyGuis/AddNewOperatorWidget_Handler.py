from AddNewOperatorWidget import Ui_addNewOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class AddNewOperatorHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_addNewOperatorWidget()
        self.ui.setupUi(self)
        self.ui.saveOperatorButton.clicked.connect(self.saveOperatorButtonClicked)
# Set QIntValidator to restrict input to integers only
        self.ui.newEmployeeNumberInput.setValidator(QIntValidator())  # Accept any integer value

    def saveOperatorButtonClicked(self):
        operatorName =  self.ui.newOperatorNameInput.text()
        employeeNumber = self.ui.newEmployeeNumberInput.text()
    
        print("New Operator Name: ",operatorName)
        print("New Employee Number: ",employeeNumber)
        self.close()


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AddNewOperatorHandler()
    widget.show()
    app.exec()