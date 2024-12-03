#Remove Customer Widget Handler
#Outstanding work:
#Change connection of data to table  - beyond this everything appears fully functional - JK

from frontend.PyGuis.RemoveCustomerWidget import Ui_removeCustomerWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class RemoveCustomerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_removeCustomerWidget()
        self.ui.setupUi(self)
        self.ui.comboBox_2.currentIndexChanged.connect(self.refreshDeleteCustomerData)

        #set visibilities
        self.ui.comboBox_2.setDisabled(False)
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

    def refreshDeleteCustomerData(self):
        idFromTable = "1"
        addr1FromTable = "2"
        addr2FromTable = "3"
        cityFromTable = "4"
        regionFromTable = "5"
        postalcodeFromTable = "6"
        countryFromTable = "7"
        phonenumberFromTable = "8"
        emailFromTable = "9"

        self.ui.removeCustomerId.setText(idFromTable)
        self.ui.removeCustomerStreetAddressLine1.setText(addr1FromTable)
        self.ui.removeCustomerStreetAddressLine2.setText(addr2FromTable) 
        self.ui.removeCustomerCity.setText(cityFromTable)    
        self.ui.removeCustomerRegion.setText(regionFromTable) 
        self.ui.removeCustomerPostalCode.setText(postalcodeFromTable) 
        self.ui.removeCustomerCountry.setText(countryFromTable)
        self.ui.removeCustomerPhoneNumber.setText(phonenumberFromTable)
        self.ui.removeCustomerEmail.setText(emailFromTable)

    def deleteCustDataMethod(self):
        #write data to database
        #Update the LHS to match the database write columns
        field1 = self.ui.removeCustomerId.text()
        field2 = self.ui.removeCustomerStreetAddressLine1.text()
        field3 = self.ui.removeCustomerStreetAddressLine2.text()
        field4 = self.ui.removeCustomerCity.text()    
        field5 = self.ui.removeCustomerRegion.text() 
        field6 = self.ui.removeCustomerPostalCode.text()
        field7 = self.ui.removeCustomerCountry.text()
        field8 = self.ui.removeCustomerPhoneNumber.text()
        field9 = self.ui.removeCustomerEmail.text()

        #confirming functionality
        print(field1)
        print(field2)
        print(field3)
        print(field4)
        print(field5)
        print(field6)
        print(field7)
        print(field8)
        print(field9)

    def deleteCustomerButtonClicked(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Delete Customer")
        msg_box.setText("Are you sure you want to delete this customer? This action cannot be undone.")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.deleteCustDataMethod()
            self.close()  # Close the widget if OK is clicked
            #Code to delete the entry from the database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked




if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = RemoveCustomerWidgetHandler()
    widget.show()
    app.exec()
