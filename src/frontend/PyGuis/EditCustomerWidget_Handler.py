#Edit Customer Handler
#Outstanding work: 
#Change connection of data to table - beyond this everything appears fully functional - JK

from frontend.PyGuis.editCustomerWidget import Ui_removeCustomerWidget


from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class EditCustomerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_removeCustomerWidget()
        self.ui.setupUi(self)

        #Update the RHS of these entities to correspond to the table entries
        #-----------------------------------------------------
        #read customer data from table
        #[Customer ID, Customer Acct name, Addr 1, Addr 2, City, Region, Postal code, Country, Phone number, Email] all strings
        #-----------------------------------------------------
        self.userData = [["ACCT1", "Account 1", "111 University Way", "A", "Kelowna", "BC", "V1V 1V1", "Canada", "111-111-1111","university1@ubc.ca"], ["ACCT2", "Account 2", "222 University Way", "B", "Kelowna", "BC", "V2V 2V2", "Canada", "222-222-2222","university2@ubc.ca"]]
        userIDs = [item[0] for item in self.userData]
        self.ui.comboBox_2.clear()
        self.ui.comboBox_2.addItems(userIDs)
        self.ui.billingCountryInput_2.addItems(["-","Canada","Other"])
        self.ui.billingRegionInput_2.addItems(["AB","BC","MB","NB","NL","NS","NT","NU","ON","PE","QC","SK","YT"])
        self.ui.comboBox_2.currentIndexChanged.connect(self.refreshEditCustomerData)
        self.refreshEditCustomerData()

        # #set default visibilities
        # self.ui.comboBox_2.setDisabled(False)
        # self.ui.removeCustomerCity.setDisabled(True)
        # self.ui.billingRegionInput_2.setDisabled(True)
        # self.ui.removeCustomerEmail.setDisabled(True)
        # self.ui.removeCustomerId.setDisabled(True)
        # self.ui.removeCustomerPhoneNumber.setDisabled(True)
        # self.ui.removeCustomerPostalCode.setDisabled(True)
        # self.ui.billingCountryInput_2.setDisabled(True)
        # self.ui.removeCustomerStreetAddressLine1.setDisabled(True)
        # self.ui.removeCustomerStreetAddressLine2.setDisabled(True)

        self.ui.deleteCustomerButton.clicked.connect(self.deleteCustomerButtonClicked)  

    def refreshEditCustomerData(self):

        selectedCustomerID = self.ui.comboBox_2.currentText()
        
        # Find matching user data from self.userData
        matching_customer = next((item for item in self.userData if item[0] == selectedCustomerID), None)
        
        # If a matching customer is found, populate the UI fields
        if matching_customer:
            self.ui.removeCustomerId.setText(matching_customer[1])  # Customer ID
            self.ui.removeCustomerStreetAddressLine1.setText(matching_customer[2])  # Street Address Line 1
            self.ui.removeCustomerStreetAddressLine2.setText(matching_customer[3])  # Street Address Line 2
            self.ui.removeCustomerCity.setText(matching_customer[4])  # City
            self.ui.billingRegionInput_2.setCurrentText(matching_customer[5])  # Region
            self.ui.removeCustomerPostalCode.setText(matching_customer[6])  # Postal Code
            self.ui.billingCountryInput_2.setCurrentText(matching_customer[7])  # Country
            self.ui.removeCustomerPhoneNumber.setText(matching_customer[8])  # Phone Number
            self.ui.removeCustomerEmail.setText(matching_customer[9])  # Email
        else:
            # Clear all fields if no matching customer is found
            self.ui.removeCustomerId.clear()
            self.ui.removeCustomerStreetAddressLine1.clear()
            self.ui.removeCustomerStreetAddressLine2.clear()
            self.ui.removeCustomerCity.clear()
            self.ui.billingRegionInput_2.clear()
            self.ui.removeCustomerPostalCode.clear()
            self.ui.billingCountryInput_2.clear()
            self.ui.removeCustomerPhoneNumber.clear()
            self.ui.removeCustomerEmail.clear()
            print("No matching customer found")

        #update screen visibilities
        # self.ui.comboBox_2.setDisabled(False)
        # self.ui.removeCustomerCity.setDisabled(False)
        # self.ui.billingRegionInput_2.setDisabled(False)
        # self.ui.removeCustomerEmail.setDisabled(False)
        # self.ui.removeCustomerId.setDisabled(False)
        # self.ui.removeCustomerPhoneNumber.setDisabled(False)
        # self.ui.removeCustomerPostalCode.setDisabled(False)
        # self.ui.billingCountryInput_2.setDisabled(False)
        # self.ui.removeCustomerStreetAddressLine1.setDisabled(False)
        # self.ui.removeCustomerStreetAddressLine2.setDisabled(False)

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
        field = ["","","","","","","","","",""]
        field[0] = self.ui.removeCustomerId.text()
        field[1] = self.ui.removeCustomerStreetAddressLine1.text()
        field[2] = self.ui.removeCustomerStreetAddressLine2.text()
        field[3] = self.ui.removeCustomerCity.text()    
        field[4] = self.ui.billingRegionInput_2.currentText() 
        field[5] = self.ui.removeCustomerPostalCode.text()
        field[6] = self.ui.billingCountryInput_2.currentText()
        field[7] = self.ui.removeCustomerPhoneNumber.text()
        field[8] = self.ui.removeCustomerEmail.text()

        print(field)

  #-----------------------------------------------------
        #James: 
        # write fieldx to database - note that this one doesn't have the account ID as the 0th element!
        #[Customer Acct Name, Add1, Add2, City, Region, Postal Code, Country, Phone number, Email]
  #-----------------------------------------------------



if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditCustomerWidgetHandler()
    widget.show()
    app.exec()
