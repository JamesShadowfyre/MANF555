from EditUserWidget import Ui_editUserWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class EditUserWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_editUserWidget()
        self.ui.setupUi(self)

        self.ui.saveChangesButton.clicked.connect(self.saveChangesButtonClicked)

    def saveChangesButtonClicked(self):
        employeeNumber = self.ui.editUserEmployeeNumber.currentText()
        userName = self.ui.editUserUsername.text()
        userRights = self.ui.editUserRights.currentText()

        print("Following User Edited: ")
        print("Employee Number: ")
        print(employeeNumber)
        print("Username: ")
        print(userName)
        print("Rights: ")
        print(userRights)
        self.close()
        
# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditUserWidgetHandler()
    widget.show()
    app.exec()