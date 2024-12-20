#Add New Customer Widget Handler

#Work remaining on this Handler:

#from frontend.PyGuis.AddCustomerWidget import Ui_AddNewCustomerWidget
from frontend.PyGuis.AddCustomerWidget import Ui_AddNewCustomerWidget
from backend.apiAccessPoint import ApplicationHome
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class AddCustomerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_AddNewCustomerWidget()
        self.ui.setupUi(self)

        self.ui.groupBox.setDisabled(False)
        self.ui.checkBox.stateChanged.connect(self.changeBillingVis)
        self.ui.pushButton.clicked.connect(self.AddNewCustSave)

    def AddNewCustSave(self, state):
        
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Add Customer")
        msg_box.setText("Please confirm that all entered information is correct. No error trapping has been implemented to this screen.")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.saveNewCustData(state)
            self.close()  # Close the widget if OK is clicked
            #Code to modify the entry from the database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked


    def changeBillingVis(self, state): #state is changed by stateChanged. Did not need to be assigned becase there's only one checkbox
        if state == 2: #"billing info is the same as account info"
            #read data from 
            self.ui.groupBox.setDisabled(True)
            fieldb1 = self.ui.accountNameInput.text()
            fieldb2 = self.ui.streetAddressLine1Input.text()
            fieldb3 = self.ui.billingStreetAddressLine2Input.text()
            fieldb4 = self.ui.lineEdit_4.text()
            fieldb5 = self.ui.regionInput.currentText()
            fieldb6 = self.ui.postalCodeInput.text()
            fieldb7 = self.ui.comboBox.currentText()
            fieldb8 = self.ui.phoneNumberInput.text()
            fieldb9 = self.ui.emailInput.text()

            self.ui.billingNameInput.setText(fieldb1)
            self.ui.billingStreetAddressLine1Input.setText(fieldb2)
            self.ui.billingStreetAddressLine2Input.setText(fieldb3)
            self.ui.billingCityInput.setText(fieldb4)
            self.ui.billingRegionInput.setCurrentText(fieldb5)
            self.ui.billingPostalCodeInput_2.setText(fieldb6)
            self.ui.billingCountryInput.setCurrentText(fieldb7)
            self.ui.billingPhoneNumberInput.setText(fieldb8)
            self.ui.billingEmailInput.setText(fieldb9)

        if state == 0:
            self.ui.groupBox.setDisabled(False)
            self.ui.billingNameInput.setText("")
            self.ui.billingStreetAddressLine1Input.setText("")
            self.ui.billingStreetAddressLine2Input.setText("")
            self.ui.billingCityInput.setText("")
            self.ui.billingRegionInput.setCurrentText("")
            self.ui.billingPostalCodeInput_2.setText("")
            self.ui.billingCountryInput.setCurrentText("-")
            self.ui.billingPhoneNumberInput.setText("")
            self.ui.billingEmailInput.setText("")

    def saveNewCustData(self, state):
        self.changeBillingVis(state) #Update the UI accordingly before written data is saved

        field = ["","","","","","","","",""]
        field[0] = self.ui.accountNameInput.text()
        field[1] = self.ui.streetAddressLine1Input.text()
        field[2] = self.ui.streetAddressLine2Input.text()
        field[3] = self.ui.lineEdit_4.text()
        field[4] = self.ui.regionInput.currentText()
        field[5] = self.ui.postalCodeInput.text()
        field[6] = self.ui.comboBox.currentText()
        field[7] = self.ui.phoneNumberInput.text()
        field[8] = self.ui.emailInput.text()


        
        #-----------------------------------------------------
        #James: 
        # write field to database - note that this one doesn't have the account ID as the 0th element!
        # [Customer Acct Name, Add1, Add2, City, Region, Postal Code, Country, Phone number, Email]
        #-----------------------------------------------------
        self.api = ApplicationHome()
        self.api.customerFunctions('create', accountName=field[0])


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AddCustomerWidgetHandler()
    widget.show()
    app.exec()



        #not including these in data tie in, just... waste of time.
        # field10 = self.ui.comboBox_2.currentText()
        # field11 = self.ui.billingNameInput.text()
        # field12 = self.ui.billingStreetAddressLine1Input.text()
        # field13 = self.ui.billingStreetAddressLine2Input.text()
        # field14 = self.ui.billingCityInput.text()
        # field15 = self.ui.billingRegionInput.currentText()
        # field16 = self.ui.billingPostalCodeInput_2.text()
        # field17 = self.ui.billingCountryInput.currentText()
        # field18 = self.ui.billingPhoneNumberInput.text()
        # field19 = self.ui.billingEmailInput.text()

        # self.ui.accountNameInput.text()
        # self.ui.streetAddressLine1Input.text()
        # self.ui.billingStreetAddressLine2Input.text()
        # self.ui.lineEdit_4.text()
        # self.ui.regionInput.currentText()
        # self.ui.postalCodeInput.text()
        # self.ui.comboBox.currentText()
        # self.ui.phoneNumberInput.text()
        # self.ui.emailInput.text()
        # self.ui.comboBox_2.currentText()
        # self.ui.billingNameInput.text()
        # self.ui.billingStreetAddressLine1Input.text()
        # self.ui.billingStreetAddressLine2Input.text()
        # self.ui.billingCityInput.text()
        # self.ui.billingRegionInput.currentText()
        # self.ui.billingPostalCodeInput_2.text()
        # self.ui.billingCountryInput.currentText()
        # self.ui.billingPhoneNumberInput.text()
        # self.ui.billingEmailInput.text()



