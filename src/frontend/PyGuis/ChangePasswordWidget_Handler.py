# needs to be connected to database to retrieve employee number list

from frontend.PyGuis.ChangePasswordWidget import Ui_ChangePasswordWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class ChangePasswordWidgetHandler(qtw.QWidget): 

    def __init__(self):
        super().__init__()
        self.ui = Ui_ChangePasswordWidget()
        self.ui.setupUi(self)
        # user data format: key : [User ID, Username, Password]
        
        userData = {"1": ["ID1", "user1", "pass1"],"2": ["ID2", "user2", "pass2"], "3": ["ID3", "user4", "pass5"]}

        self.ui.changePasswordPassword.setDisabled(True)
        self.ui.changePasswordUsername.setDisabled(True)

        self.ui.changePasswordEmployeeNumber.addItems([value[1] for value in userData.values()])

        self.ui.savePasswordButton.clicked.connect(self.savePasswordButtonClicked)
        


        self.ui.changePasswordEmployeeNumber.currentTextChanged.connect(self.updateUI)

    
    def updateUI(self,t1):
            self.ui.changePasswordPassword.setDisabled(False)
            selectedUserID = self.ui.changePasswordEmployeeNumber.currentText()



    def savePasswordButtonClicked(self):
        employeeNumber = self.ui.changePasswordEmployeeNumber.currentText()
        userName = self.ui.changePasswordUsername.text()
        password = self.ui.changePasswordPassword.text()

        print("Password changed for following user: ")
        print("Employee Number: ", employeeNumber)
        print("Username: ", userName)
        print("Password: ", "*" * len(password))
        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ChangePasswordWidgetHandler()
    widget.show()
    app.exec()