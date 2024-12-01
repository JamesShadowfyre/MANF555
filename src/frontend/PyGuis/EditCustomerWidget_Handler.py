#Edit Customer Handler
#Outstanding work:
#Change connection of data to table - beyond this everything appears fully functional - JK

from editCustomerWidget import Ui_removeCustomerWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class EditCustomerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_removeCustomerWidget()
        self.ui.setupUi(self)

        #self.refreshEditCustomerData()

        self.ui.comboBox_2.currentIndexChanged.connect(self.refreshEditCustomerData)

        #set default visibilities
        self.ui.comboBox_2.setDisabled(False)
        self.ui.removeCustomerCity.setDisabled(True)
        self.ui.billingRegionInput_2.setDisabled(True)
        self.ui.removeCustomerEmail.setDisabled(True)
        self.ui.removeCustomerId.setDisabled(True)
        self.ui.removeCustomerPhoneNumber.setDisabled(True)
        self.ui.removeCustomerPostalCode.setDisabled(True)
        self.ui.billingCountryInput_2.setDisabled(True)
        self.ui.removeCustomerStreetAddressLine1.setDisabled(True)
        self.ui.removeCustomerStreetAddressLine2.setDisabled(True)

        self.ui.deleteCustomerButton.clicked.connect(self.deleteCustomerButtonClicked)  

    def refreshEditCustomerData(self):
        #Update the RHS of these entities to correspond to the table entries
        idFromTable = "1"
        addr1FromTable = "2"
        addr2FromTable = "3"
        cityFromTable = "4"
        regionFromTable = "NB"
        postalcodeFromTable = "6"
        countryFromTable = "Canada"
        phonenumberFromTable = "8"
        emailFromTable = "9"

        self.ui.removeCustomerId.setText(idFromTable)
        self.ui.removeCustomerStreetAddressLine1.setText(addr1FromTable)
        self.ui.removeCustomerStreetAddressLine2.setText(addr2FromTable) 
        self.ui.removeCustomerCity.setText(cityFromTable)    
        self.ui.billingRegionInput_2.setCurrentText(regionFromTable) 
        self.ui.removeCustomerPostalCode.setText(postalcodeFromTable) 
        self.ui.billingCountryInput_2.setCurrentText(countryFromTable)
        self.ui.removeCustomerPhoneNumber.setText(phonenumberFromTable)
        self.ui.removeCustomerEmail.setText(emailFromTable)

        #update screen visibilities
        self.ui.comboBox_2.setDisabled(False)
        self.ui.removeCustomerCity.setDisabled(False)
        self.ui.billingRegionInput_2.setDisabled(False)
        self.ui.removeCustomerEmail.setDisabled(False)
        self.ui.removeCustomerId.setDisabled(False)
        self.ui.removeCustomerPhoneNumber.setDisabled(False)
        self.ui.removeCustomerPostalCode.setDisabled(False)
        self.ui.billingCountryInput_2.setDisabled(False)
        self.ui.removeCustomerStreetAddressLine1.setDisabled(False)
        self.ui.removeCustomerStreetAddressLine2.setDisabled(False)

    def deleteCustomerButtonClicked(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Edit Customer")
        msg_box.setText("Are you sure you want to save these changes? This action cannot be undone.")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.saveCustomerDataEditMethod()
            self.close()  # Close the widget if OK is clicked
            #Code to modify the entry from the database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked

    def saveCustomerDataEditMethod(self):
        #write data to database
        #Update the LHS to match the database write columns
        field1 = self.ui.removeCustomerId.text()
        field2 = self.ui.removeCustomerStreetAddressLine1.text()
        field3 = self.ui.removeCustomerStreetAddressLine2.text()
        field4 = self.ui.removeCustomerCity.text()    
        field5 = self.ui.billingRegionInput_2.currentText() 
        field6 = self.ui.removeCustomerPostalCode.text()
        field7 = self.ui.billingCountryInput_2.currentText()
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



if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditCustomerWidgetHandler()
    widget.show()
    app.exec()
