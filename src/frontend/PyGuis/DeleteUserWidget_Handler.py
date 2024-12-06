# needs to be connected to database to retrieve user  list

#from frontend.PyGuis.ChangePasswordWidget import Ui_ChangePasswordWidget
from DeleteUserWidget import Ui_ChangePasswordWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class DeleteWidgetHandler(qtw.QWidget): 

    def __init__(self):
        super().__init__()
        self.ui = Ui_ChangePasswordWidget()
        self.ui.setupUi(self)
        
        #-----------------------------------------------------
        #Replace RHS of self.userData with the tie in
        #[User ID, Username]
        #----------------------------------------------------- 
        #user data format: key : [User ID, Username]
        self.userData = [["ID1", "user1"], ["ID2", "user2"], ["ID3", "user3"]]
        IDs = [item[0] for item in self.userData]


        # Disable the password and username fields initially
        self.ui.changePasswordPassword.setDisabled(True)
        self.ui.changePasswordUsername.setDisabled(True)
        self.ui.changePasswordPassword.setVisible(False)
        self.ui.label_11.setVisible(False)

        # Add usernames to the combo box
    
        self.ui.changePasswordEmployeeNumber.addItems(IDs)

        # Connect button and combobox signals
        self.ui.savePasswordButton.clicked.connect(self.savePasswordButtonClicked)
        self.ui.changePasswordEmployeeNumber.currentTextChanged.connect(self.updateUI)

        #perform initial fill of data
        selectedUserID = self.ui.changePasswordEmployeeNumber.currentText()

        matching_id = next((item[1] for item in self.userData if item[0] == selectedUserID), None)
        if matching_id:
            self.ui.changePasswordUsername.setText(matching_id)
        else:
            self.ui.changePasswordUsername.clear()
            print(matching_id)
            self.ui.changePasswordUsername.setText(matching_id)

    def updateUI(self, t1):
        # Enable the password field once a user is selected
        self.ui.changePasswordPassword.setDisabled(False)
        selectedUserID = self.ui.changePasswordEmployeeNumber.currentText()

        matching_id = next((item[1] for item in self.userData if item[0] == selectedUserID), None)

        if matching_id:
        # Set the username field with the corresponding username
            self.ui.changePasswordUsername.setText(matching_id)
        else:
        # Clear the username field if no match is found
            self.ui.changePasswordUsername.clear()
            print(matching_id)
            self.ui.changePasswordUsername.setText(matching_id)


    def savePasswordButtonClicked(self):
        employeeSaveData = ["","",""]
        employeeSaveData[0] = self.ui.changePasswordEmployeeNumber.currentText() #employee ID - change to database entry
        employeeSaveData[1] = self.ui.changePasswordUsername.text() # employee Name change to database entry
 
  #-----------------------------------------------------
        #write employeeSaveData to database
        #[User ID, Username]
  #-----------------------------------------------------

        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Delete User")
        msg_box.setText("Are you sure you wish to delete this user? This action cannot be undone?")
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:   
            self.close()  # Close the widget if OK is clicked

        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = DeleteWidgetHandler()
    widget.show()
    app.exec()
