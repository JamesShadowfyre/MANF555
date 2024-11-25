#Remove Customer Widget Handler
#Change connection of data to table
#For some reason the setText functions aren't working in this file, even though it is an identical application to the LowInventoryAlarmSettingWidget, which functions just fine...

from RemoveCustomerWidget import Ui_removeCustomerWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class RemoveCustomerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_removeCustomerWidget()
        self.ui.setupUi(self)

        self.ui.comboBox_2.setItemText = "test"
        self.ui.removeCustomerCity.setText = "1"
        self.ui.removeCustomerCountry.setText = "2"
        self.ui.removeCustomerEmail.setText = "3"
        self.ui.removeCustomerId.setText = "4"
        self.ui.removeCustomerPhoneNumber.setText = "5"
        self.ui.removeCustomerPostalCode.setText = "6"
        self.ui.removeCustomerRegion.setText = "7"
        self.ui.removeCustomerStreetAddressLine1.setText = "8"
        self.ui.removeCustomerStreetAddressLine2.setText = "9"

        self.ui.comboBox_2.setDisabled(True)
        self.ui.removeCustomerCity.setDisabled(True)
        self.ui.removeCustomerCountry.setDisabled(True)
        self.ui.removeCustomerEmail.setDisabled(True)
        self.ui.removeCustomerId.setDisabled(True)
        self.ui.removeCustomerPhoneNumber.setDisabled(True)
        self.ui.removeCustomerPostalCode.setDisabled(True)
        self.ui.removeCustomerRegion.setDisabled(True)
        self.ui.removeCustomerStreetAddressLine1.setDisabled(True)
        self.ui.removeCustomerStreetAddressLine2.setDisabled(True)

        self.ui.deleteCustomerButton.clicked.connect(self.deleteCustomerButtonClicked)  


    def deleteCustomerButtonClicked(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Delete Customer")
        msg_box.setText("Are you sure you want to delete this customer? This action cannot be undone.")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.close()  # Close the widget if OK is clicked
            #Code to delete the entry from the database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked




if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = RemoveCustomerWidgetHandler()
    widget.show()
    app.exec()
