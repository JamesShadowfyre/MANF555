# LoginWindow Handler

#I'm struggling to debug the non-functioning usernameInput Text Input field. It loses functionality whenever I click anywhere.
#I've ensured the field is enabled, I've tried setting focus to the object, I've set read only to False,changed exec_ to show_ for the Qmessage, 
#I ran the code thorugh chatgpt, didn't resolve the issue, worked through all 7 suggested remedies and none of them worked.
#There is something fundamentally wrong here that i have no idea how to fix. I would've killed to have had more in-class instruction.  

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
        pass
  
if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = loginWindowHandler()
    widget.show()
    app.exec()