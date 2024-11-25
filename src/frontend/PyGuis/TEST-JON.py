from PyQt5 import QtWidgets as qtw
import NewUserWidget_Handler
import NewUserWidget
from UserManagerWidget import Ui_UserManagerWidget

class NewUserWidgetHandler(qtw.QDialog):  # Inherit from QDialog instead of QWidget
    def __init__(self):
        super().__init__()

        # Your existing UI setup logic
        self.setWindowTitle("New User")
        self.setGeometry(100, 100, 300, 200)
        self.setModal(True)  # Now you can use setModal because it's a QDialog
        self.ui = NewUserWidget.Ui_newUserWidget()  # Assuming you have a Ui_NewUserWidget
        self.ui.setupUi(self)
        # Any additional initialization for your new user form



class UserManagerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_UserManagerWidget()
        self.ui.setupUi(self)
        self.ui.newUserButton.clicked.connect(self.newUserButtonClicked)
        self.ui.exitUserManagerButton.clicked.connect(self.exitUserManagerButtonClicked)
        self.ui.changeUserPassword.clicked.connect(self.changeUserPasswordButtonClicked)
        self.ui.removeUserButton.clicked.connect(self.removeUserButtonClicked)

    def newUserButtonClicked(self):
        # Disable the main window
        self.setEnabled(False)
        
        # Create and show the New User window (modal)
        self.new_user_widget = NewUserWidgetHandler()
        self.new_user_widget.exec_()  # Blocks interaction with the main window
        
        # Re-enable the main window after the new window is closed
        self.setEnabled(True)

    def exitUserManagerButtonClicked(self): 
        self.close()

    def changeUserPasswordButtonClicked(self):
        print("change password button pressed")

    def removeUserButtonClicked(self):
        print("remove user button pressed")

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = UserManagerWidgetHandler()
    widget.show()
    app.exec()
