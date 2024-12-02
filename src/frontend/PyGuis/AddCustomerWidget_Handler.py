#Add New Customer Widget Handler

#Work remaining on this Handler:

from frontend.PyGuis.AddCustomerWidget import Ui_AddNewCustomerWidget
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

    def saveNewCustData(self):
        self.changeBillingVis() #Update the UI accordingly

        field1 = self.ui.accountNameInput.text()
        field2 = self.ui.streetAddressLine1Input.text()
        field3 = self.ui.billingStreetAddressLine2Input.text()
        field4 = self.ui.lineEdit_4.text()
        field5 = self.ui.regionInput.currentText()
        field6 = self.ui.postalCodeInput.text()
        field7 = self.ui.comboBox.currentText()
        field8 = self.ui.phoneNumberInput.text()
        field9 = self.ui.emailInput.text()
        field10 = self.ui.comboBox_2.currentText()
        field11 = self.ui.billingNameInput.text()
        field12 = self.ui.billingStreetAddressLine1Input.text()
        field13 = self.ui.billingStreetAddressLine2Input.text()
        field14 = self.ui.billingCityInput.text()
        field15 = self.ui.billingRegionInput.currentText()
        field16 = self.ui.billingPostalCodeInput_2.text()
        field17 = self.ui.billingCountryInput.currentText()
        field18 = self.ui.billingPhoneNumberInput.text()
        field19 = self.ui.billingEmailInput.text()

        self.ui.accountNameInput.text()
        self.ui.streetAddressLine1Input.text()
        self.ui.billingStreetAddressLine2Input.text()
        self.ui.lineEdit_4.text()
        self.ui.regionInput.currentText()
        self.ui.postalCodeInput.text()
        self.ui.comboBox.currentText()
        self.ui.phoneNumberInput.text()
        self.ui.emailInput.text()
        self.ui.comboBox_2.currentText()
        self.ui.billingNameInput.text()
        self.ui.billingStreetAddressLine1Input.text()
        self.ui.billingStreetAddressLine2Input.text()
        self.ui.billingCityInput.text()
        self.ui.billingRegionInput.currentText()
        self.ui.billingPostalCodeInput_2.text()
        self.ui.billingCountryInput.currentText()
        self.ui.billingPhoneNumberInput.text()
        self.ui.billingEmailInput.text()

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AddCustomerWidgetHandler()
    widget.show()
    app.exec()



