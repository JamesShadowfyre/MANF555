# needs to be connected to database to retrieve used data

from frontend.PyGuis.ChangePasswordWidget import Ui_ChangePasswordWidget
#from ChangePasswordWidget import Ui_ChangePasswordWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class ChangePasswordWidgetHandler(qtw.QWidget): 

    def __init__(self):
        super().__init__()
        self.ui = Ui_ChangePasswordWidget()
        self.ui.setupUi(self)
        
     #-----------------------------------------------------
        #read employeeSaveData from database
        #Replace RHS of self.userData
        #[User ID, Username]
     #-----------------------------------------------------
        self.userData = [["ID1", "user1"], ["ID2", "user2"], ["ID3", "user3"]]
        IDs = [item[0] for item in self.userData]

        # Disable the password and username fields initially
        self.ui.changePasswordPassword.setDisabled(True)
        self.ui.changePasswordUsername.setDisabled(True)

        # Add usernames to the combo box
        self.ui.changePasswordEmployeeNumber.addItems(IDs)

        # Connect button and combobox signals
        self.ui.savePasswordButton.clicked.connect(self.savePasswordButtonClicked)
        self.ui.changePasswordEmployeeNumber.currentTextChanged.connect(self.updateUI)

        #this does the initial check to populate the screen employee user field
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


    def savePasswordButtonClicked(self):
        employeeSaveData = ["","",""]
        employeeSaveData[0] = self.ui.changePasswordEmployeeNumber.currentText() #employee ID - change to database entry
        employeeSaveData[1] = self.ui.changePasswordUsername.text() # employee Name change to database entry
        employeeSaveData[2] = self.ui.changePasswordPassword.text() # employee password change to database entry

  #-----------------------------------------------------
        #write employeeSaveData to database
        #[User ID, Username, Password]
  #-----------------------------------------------------

        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ChangePasswordWidgetHandler()
    widget.show()
    app.exec()
