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

        #-----------------------------------------------------
        #James: 
        # read from customers table in database, in this order as userData
        # [Customer Acct Name, Add1, Add2, City, Region, Postal Code, Country, Phone number, Email] - all str
        #-----------------------------------------------------

        self.userData = [["ACCT1", "Account 1", "111 University Way", "A", "Kelowna", "BC", "V1V 1V1", "Canada", "111-111-1111","university1@ubc.ca"], ["ACCT2", "Account 2", "222 University Way", "B", "Kelowna", "BC", "V2V 2V2", "Canada", "222-222-2222","university2@ubc.ca"]]
        

        userIDs = [item[0] for item in self.userData]
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(userIDs)
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
        self.refreshDeleteCustomerData()

    def refreshDeleteCustomerData(self):
        selectedCustomerID = self.ui.comboBox_2.currentText()
        
        # Find matching user data from self.userData
        matching_customer = next((item for item in self.userData if item[0] == selectedCustomerID), None)
        
        # If a matching customer is found, populate the UI fields
        if matching_customer:
            self.ui.removeCustomerId.setText(matching_customer[1])  # Customer ID
            self.ui.removeCustomerStreetAddressLine1.setText(matching_customer[2])  # Street Address Line 1
            self.ui.removeCustomerStreetAddressLine2.setText(matching_customer[3])  # Street Address Line 2
            self.ui.removeCustomerCity.setText(matching_customer[4])  # City
            self.ui.removeCustomerRegion.setText(matching_customer[5])  # Region
            self.ui.removeCustomerPostalCode.setText(matching_customer[6])  # Postal Code
            self.ui.removeCustomerCountry.setText(matching_customer[7])  # Country
            self.ui.removeCustomerPhoneNumber.setText(matching_customer[8])  # Phone Number
            self.ui.removeCustomerEmail.setText(matching_customer[9])  # Email
        else:
            # Clear all fields if no matching customer is found
            self.ui.removeCustomerId.clear()
            self.ui.removeCustomerStreetAddressLine1.clear()
            self.ui.removeCustomerStreetAddressLine2.clear()
            self.ui.removeCustomerCity.clear()
            self.ui.removeCustomerRegion.clear()
            self.ui.removeCustomerPostalCode.clear()
            self.ui.removeCustomerCountry.clear()
            self.ui.removeCustomerPhoneNumber.clear()
            self.ui.removeCustomerEmail.clear()
            print("No matching customer found")

    def deleteCustDataMethod(self):
        #write data to database
        #Update the LHS to match the database write columns
        field = ["","","","","","","","",""]
        field[0] = self.ui.removeCustomerId.text()
        field[1] = self.ui.removeCustomerStreetAddressLine1.text()
        field[2] = self.ui.removeCustomerStreetAddressLine2.text()
        field[3] = self.ui.removeCustomerCity.text()    
        field[4] = self.ui.removeCustomerRegion.text() 
        field[5] = self.ui.removeCustomerPostalCode.text()
        field[6] = self.ui.removeCustomerCountry.text()
        field[7] = self.ui.removeCustomerPhoneNumber.text()
        field[8] = self.ui.removeCustomerEmail.text()

        #confirming functionality
        print(field)

                
        #-----------------------------------------------------
        #James: 
        # write field to database, in this order
        # [Customer Acct Name, Add1, Add2, City, Region, Postal Code, Country, Phone number, Email] - all str
        #-----------------------------------------------------

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
