#New User Widget handler
#Successfully can access the information entered by the user... only update required is to add save directories to SQL table for the 4 pieces of info

from frontend.PyGuis.NewUserWidget import Ui_newUserWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class NewUserWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_newUserWidget()
        self.ui.setupUi(self)
        self.ui.saveNewUserButton.clicked.connect(self.SaveNewUserButtonClicked)
# Set QIntValidator to restrict input to integers only
        self.ui.lineEdit_3.setValidator(QIntValidator())  # Accept any integer value

    def SaveNewUserButtonClicked(self):
        #read data from user inputs
        employeeNumber = self.ui.lineEdit_3.text()
        username = self.ui.newUserUsername.text()
        rights = self.ui.editUserRights_2.currentText()
        password = self.ui.lineEdit_2.text()
        
        #confirming that this works
        print("Following User Added: ")
        print("Employee Number: ",employeeNumber)
        print("Username: ",username)
        print("Rights: ",rights)
        print("Password: ",  "*" * len(password))
        pass

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = NewUserWidgetHandler()
    widget.show()
    app.exec()
