#User Manager Widget


# import secondary widget handlers
from frontend.PyGuis.UserManagerWidget import Ui_UserManagerWidget
from frontend.PyGuis.NewUserWidget_Handler import NewUserWidgetHandler
from frontend.PyGuis.ChangePasswordWidget_Handler import ChangePasswordWidgetHandler
from frontend.PyGuis.DeleteUserWidget_Handler import DeleteWidgetHandler

# from UserManagerWidget import Ui_UserManagerWidget
# from NewUserWidget_Handler import NewUserWidgetHandler
# from ChangePasswordWidget_Handler import ChangePasswordWidgetHandler
# from DeleteUserWidget_Handler import DeleteWidgetHandler
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

        #-----------------------------------------------------
        #Replace RHS of self.userData with the tie in
        #[User ID, Username, Rights [Bool]
        #----------------------------------------------------- 
        self.userData = [["ID1", "user1",0], ["ID2", "user2",0], ["ID3", "user3",0]]
        
        #Table Operations Begin -----
        # Clear the table before populating
        self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget.setRowCount(len(self.userData))
        self.ui.tableWidget.setColumnCount(3)  # Adjust columns if necessary
        self.ui.tableWidget.setHorizontalHeaderLabels(["User ID", "Username", "Admin Rights"]) 

        # Populate the table
        for row, data in enumerate(self.userData):
            for column, value in enumerate(data):
                # Convert rights (column 2) to human-readable text, e.g., Yes/No
                if column == 2:  # Assuming rights is the third column
                    item = qtw.QTableWidgetItem("Yes" if value else "No")
                else:
                    item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        #Table Operations End -----
        #  
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


    def removeUserButtonClicked(self):
        self.remove_user_widget = DeleteWidgetHandler()
        self.remove_user_widget.show()
        print("remove user button pressed")
    

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = UserManagerWidgetHandler()
    widget.show()
    app.exec()
