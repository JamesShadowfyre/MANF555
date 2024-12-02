# LoginWindow Handler

#I'm struggling to debug the non-functioning usernameInput Text Input field. It loses functionality whenever I click anywhere.
#I've ensured the field is enabled, I've tried setting focus to the object, I've set read only to False,changed exec_ to show_ for the Qmessage, 
#I ran the code thorugh chatgpt, didn't resolve the issue, worked through all 7 suggested remedies and none of them worked.
#There is something fundamentally wrong here that i have no idea how to fix. I would've killed to have had more in-class instruction.  
from MainWindow_Handler import MainWindow
from LoginWindow import Ui_loginWindow
from PyQt5 import QtWidgets as qtw

class loginWindowHandler(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)
        
        self.ui.usernameInput.show()  # Make sure the text input is visible
        self.ui.usernameInput.setReadOnly(False) #make sure that it is not read only
        self.ui.usernameInput.setEnabled(True) #make sure is enabled
 
        # Connect the "Forgot Password" button to the forgotPassword method
        self.ui.forgotPasswordButton.clicked.connect(self.forgotPasswordAction)
        self.ui.loginButton.clicked.connect(self.loginAction)

    def forgotPasswordAction(self):
        qtw.QMessageBox.information(self,"Forgot Password", "Please contact Administrator for password reset")

    def loginAction(self): 
        loginEntry = self.ui.usernameInput.text() 
        passwordEntry = self.ui.passwordInput.text()

        # Define the login data
        loginUserdata = {"jonk": 123, "morganm": 456, "jamesr": 789}

# Validate the username and password
        try:
            if loginEntry in loginUserdata:
                # Ensure type consistency before comparison
                if int(passwordEntry) == loginUserdata[loginEntry]:

                    self.login = MainWindow()
                    self.login.show()
                else:
                    msg_box = qtw.QMessageBox(self)
                    msg_box.setWindowTitle("GMES Login")
                    msg_box.setText("Incorrect Username or password")
                    msg_box.exec_()
            else:
                
                msg_box = qtw.QMessageBox(self)
                msg_box.setWindowTitle("GMES Login")
                msg_box.setText("Incorrect Username or password")
                msg_box.exec_()

        except (ValueError, KeyError) as e:
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("GMES Login")
            msg_box.setText("Incorrect Username or password")
            msg_box.exec_()

if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = loginWindowHandler()
    widget.show()
    app.exec()
