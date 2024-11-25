#User Manager Widget
#Need to connect this to open other screens... which need to be built still

import NewUserWidget_Handler
from UserManagerWidget import Ui_UserManagerWidget
from PyQt5 import QtWidgets as qtw

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
        self.setDisabled = (True)
        self.new_user_widget = NewUserWidget_Handler.NewUserWidgetHandler()
        self.new_user_widget.show()
        self.setModal(True)
        self.setEnabled=(True)


    def exitUserManagerButtonClicked(self): 
        self.close()

    def changeUserPasswordButtonClicked(self):
        #self.change_password_widget = 
        #self.change_password_widget.show()
        print("change password button pressed")

    def removeUserButtonClicked(self):
        #self.remove_user_widget = 
        #self.remove_user_widget.show()
       print("remove user button pressed")
    



if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = UserManagerWidgetHandler()
    widget.show()
    app.exec()
