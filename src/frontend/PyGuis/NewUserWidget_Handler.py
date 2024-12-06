#New User Widget handler
#Successfully can access the information entered by the user... only update required is to add save directories to SQL table for the 4 pieces of info

from frontend.PyGuis.NewUserWidget import Ui_newUserWidget
#from NewUserWidget import Ui_newUserWidget
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
        userData = ["","",False,""]

        if  self.ui.editUserRights_2.currentText() == "Admin":
            userData[2] = True
        if self.ui.editUserRights_2.currentText() == "User":
            userData[2] = False
        if self.ui.editUserRights_2.currentText() != "User" and self.ui.editUserRights_2.currentText() != "Admin":
            print("error")

        userData[0] = self.ui.lineEdit_3.text()
        userData[1] = self.ui.newUserUsername.text()
        userData[3] = self.ui.lineEdit_2.text()

        self.close()


  #-----------------------------------------------------
        #write userData to database
        #[User ID, Username, rights, password] - rights is boolean, the rest are strings
  #-----------------------------------------------------     


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = NewUserWidgetHandler()
    widget.show()
    app.exec()
