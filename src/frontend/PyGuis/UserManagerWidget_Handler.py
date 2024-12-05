#User Manager Widget
#Need to connect this to open other screens... which need to be built still


from frontend.PyGuis.UserManagerWidget import Ui_UserManagerWidget
from PyQt5 import QtWidgets as qtw
# import secondary widget handlers
from frontend.PyGuis.NewUserWidget_Handler import NewUserWidgetHandler
from frontend.PyGuis.ChangePasswordWidget_Handler import ChangePasswordWidgetHandler


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
        self.new_user_widget = NewUserWidgetHandler()
        self.new_user_widget.show()
        self.setEnabled=(True)

    def exitUserManagerButtonClicked(self): 
        self.close()

    def changeUserPasswordButtonClicked(self):
        self.change_password_widget = ChangePasswordWidgetHandler()
        self.change_password_widget.show()
        # print("change password button pressed")

    def removeUserButtonClicked(self):
        #self.remove_user_widget = 
        #self.remove_user_widget.show()
        print("remove user button pressed")
    



if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = UserManagerWidgetHandler()
    widget.show()
    app.exec()
