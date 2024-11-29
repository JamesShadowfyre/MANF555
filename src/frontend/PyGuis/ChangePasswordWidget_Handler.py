# needs to be connected to database to retrieve employee number list

from ChangePasswordWidget import Ui_ChangePasswordWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class ChangePasswordWidgetHandler(qtw.QWidget): 

    def __init__(self):
        super().__init__()
        self.ui = Ui_ChangePasswordWidget()
        self.ui.setupUi(self)

        self.ui.savePasswordButton.clicked.connect(self.savePasswordButtonClicked)

    def savePasswordButtonClicked(self):
        employeeNumber = self.ui.changePasswordEmployeeNumber.currentText()
        userName = self.ui.changePasswordUsername.text()
        password = self.ui.changePasswordPassword.text()

        print("Password changed for following user: ")
        print("Employee Number: ")
        print(employeeNumber)
        print("Username: ")
        print(userName)
        print("Password: ")
        print("*" * len(password))
        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ChangePasswordWidgetHandler()
    widget.show()
    app.exec()