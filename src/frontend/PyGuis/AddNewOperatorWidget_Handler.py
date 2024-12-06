from frontend.PyGuis.AddNewOperatorWidget import Ui_addNewOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class AddNewOperatorHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_addNewOperatorWidget()
        self.ui.setupUi(self)
# Set QIntValidator to restrict input to integers only
        self.ui.newEmployeeNumberInput.setValidator(QIntValidator())  # Accept any integer value

        self.ui.saveOperatorButton.clicked.connect(self.AddNewOperatorSave)

    def AddNewOperatorSave(self, state):
    
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Add Operator")
        msg_box.setText("Please confirm that all entered information is correct. No error trapping has been implemented to this screen.")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.saveNewOperatorData(state)
            self.close()  # Close the widget if OK is clicked
            #Code to modify the entry from the database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked
    
    def saveNewOperatorData(self, state):
        field = ["","","","","","","","",""]
        field[0] = self.ui.newOperatorNameInput.text()
        field[1] = self.ui.newEmployeeNumberInput.text()
               
        operatorName =  self.ui.newOperatorNameInput.text()
        employeeNumber = self.ui.newEmployeeNumberInput.text()
    
        print("New Operator Name: ",operatorName)
        print("New Employee Number: ",employeeNumber)

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AddNewOperatorHandler()
    widget.show()
    app.exec()

