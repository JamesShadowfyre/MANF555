from frontend.PyGuis.EditOperatorWidget import Ui_editOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class EditOperatorWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_editOperatorWidget()
        self.ui.setupUi(self)
        # Set QIntValidator to restrict input to integers only
        self.ui.editEmployeeNumberInput.setValidator(QIntValidator())  # Accept any integer value

        #Update the RHS of these entities to correspond to the table entries
        #-----------------------------------------------------
        #read customer data from table
        #[Customer ID, Customer Acct name, Addr 1, Addr 2, City, Region, Postal code, Country, Phone number, Email] all strings
        #-----------------------------------------------------
        self.userData = [["jRopotar", "0479"], ["jKettle", "1542"], ["mDavis", "0869"]]
        IDs = [item[0] for item in self.userData]

        #set default visibilities
        self.ui.editEmployeeNumberInput.setDisabled(False)

# Add usernames to the combo box
    
        self.ui.editOperatorNameInput.addItems(IDs)

        # Connect button and combobox signals
        self.ui.saveOperatorButton.clicked.connect(self.saveOperatorButtonClicked)
        self.ui.editOperatorNameInput.currentTextChanged.connect(self.updateUI)

        #perform initial fill of data
        selectedUserID = self.ui.editOperatorNameInput.currentText()

        matching_id = next((item[1] for item in self.userData if item[0] == selectedUserID), None)
        if matching_id:
            self.ui.editEmployeeNumberInput.setText(matching_id)
        else:
            self.ui.editEmployeeNumberInput.clear()
            print(matching_id)
            self.ui.editEmployeeNumberInput.setText(matching_id)

    def updateUI(self, t1):
        # Enable the password field once a user is selected
        # self.ui.changePasswordPassword.setDisabled(False)
        selectedUserID = self.ui.editOperatorNameInput.currentText()

        matching_id = next((item[1] for item in self.userData if item[0] == selectedUserID), None)

        if matching_id:
        # Set the username field with the corresponding username
            self.ui.editEmployeeNumberInput.setText(matching_id)
        else:
        # Clear the username field if no match is found
            self.ui.editEmployeeNumberInput.clear()
            print(matching_id)
            self.ui.editEmployeeNumberInput.setText(matching_id)

    def saveOperatorButtonClicked(self):
        
        employeeSaveData = ["","",""]
        employeeSaveData[0] = self.ui.editOperatorNameInput.currentText() #employee ID - change to database entry
        employeeSaveData[1] = self.ui.editEmployeeNumberInput.text() # employee Name change to database entry
 
  #-----------------------------------------------------
        #write employeeSaveData to database
        #[User ID, Username]
  #-----------------------------------------------------

        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Edit User")
        msg_box.setText("Are you sure you wish to edit this user? This action cannot be undone?")
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok: 
            operatorName =  self.ui.editOperatorNameInput.currentText()
            employeeNumber = self.ui.editEmployeeNumberInput.text()
            print("Edited Operator Name: ",operatorName)
            print("Edited Employee Number: ",employeeNumber)
            self.close()  # Close the widget if OK is clicked
        
        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditOperatorWidgetHandler()
    widget.show()
    app.exec()