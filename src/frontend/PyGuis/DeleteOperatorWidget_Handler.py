from frontend.PyGuis.DeleteOperatorWidget import Ui_DeleteOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class DeleteOperatorWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteOperatorWidget()
        self.ui.setupUi(self)
    
        #Update the RHS of these entities to correspond to the table entries
        #-----------------------------------------------------
        #read customer data from table
        #[Customer ID, Customer Acct name, Addr 1, Addr 2, City, Region, Postal code, Country, Phone number, Email] all strings
        #-----------------------------------------------------
        self.userData = [["jRopotar", "0479"], ["jKettle", "1542"], ["mDavis", "0869"]]
        IDs = [item[0] for item in self.userData]

        #set default visibilities
        self.ui.deleteEmployeeNumberBox.setDisabled(True)
        

# Add usernames to the combo box
    
        self.ui.deleteOperatorComboBox.addItems(IDs)

        # Connect button and combobox signals
        self.ui.deleteOperatorButton.clicked.connect(self.deleteOperatorButtonClicked)
        self.ui.deleteOperatorComboBox.currentTextChanged.connect(self.updateUI)

        #perform initial fill of data
        selectedUserID = self.ui.deleteOperatorComboBox.currentText()

        matching_id = next((item[1] for item in self.userData if item[0] == selectedUserID), None)
        if matching_id:
            self.ui.deleteEmployeeNumberBox.setText(matching_id)
        else:
            self.ui.deleteEmployeeNumberBox.clear()
            print(matching_id)
            self.ui.deleteEmployeeNumberBox.setText(matching_id)

    def updateUI(self, t1):
        # Enable the password field once a user is selected
        # self.ui.changePasswordPassword.setDisabled(False)
        selectedUserID = self.ui.deleteOperatorComboBox.currentText()

        matching_id = next((item[1] for item in self.userData if item[0] == selectedUserID), None)

        if matching_id:
        # Set the username field with the corresponding username
            self.ui.deleteEmployeeNumberBox.setText(matching_id)
        else:
        # Clear the username field if no match is found
            self.ui.deleteEmployeeNumberBox.clear()
            print(matching_id)
            self.ui.deleteEmployeeNumberBox.setText(matching_id)

    def deleteOperatorButtonClicked(self):
        employeeSaveData = ["","",""]
        employeeSaveData[0] = self.ui.deleteOperatorComboBox.currentText() #employee ID - change to database entry
        employeeSaveData[1] = self.ui.deleteEmployeeNumberBox.text() # employee Name change to database entry
 
  #-----------------------------------------------------
        #write employeeSaveData to database
        #[User ID, Username]
  #-----------------------------------------------------

        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Delete User")
        msg_box.setText("Are you sure you wish to delete this user? This action cannot be undone?")
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok: 
            operatorName =  self.ui.deleteOperatorComboBox.currentText()
            employeeNumber = self.ui.deleteEmployeeNumberBox.text()
            print("Deleted Operator Name: ",operatorName)
            print("Deleted Employee Number: ",employeeNumber)
            self.close()  # Close the widget if OK is clicked

        self.close()
       

# Code to launch widget
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = DeleteOperatorWidgetHandler()
    widget.show()
    app.exec()