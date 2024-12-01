#Create Work Order Widget Handler

"""
Remaining work:
- Update local variables to use database table connections
- Not sure what trigger to use to get the checkbox to change... should probably just delete this feature
- need to get the error trapping working better for checking for valid inputs on the date functions, and the check for the 0 qty. Qspin Box to int conversion?
"""

from CreateWorkOrderWidgetrev6 import Ui_CreateWorkOrderWidget
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets as qtw

class CreateNewWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        self.ui.createWOCustomerSelection.addItems(["Steve", "Bob", "Joe"]) #change this with actual items from table
        self.ui.comboBox_2.addItems(["", "No drilling", "2x back holes", "2x front holes", "4x holes (2x front + 2x back)"])
        self.ui.backCaseComboBox.addItems(["","Black"])
        
        #setting the screen dates
        today = QDate.currentDate()
        self.ui.createWORequiredByDate.setDate(today)
        self.ui.createWOProductionDateInput.setDate(today)
        self.ui.createWODateInput.setDate(today)

        #Drilling station is the only station that's setup, disabling all others except for case selection
        self.ui.createNewWOSaveButton.clicked.connect(self.SaveNewWorkWorder)
        self.ui.checkBox_3.setDisabled(True)
        self.ui.checkBox_4.setEnabled(True)
        self.ui.checkBox_5.setEnabled(True) 
        self.ui.checkBox_6.setDisabled(True)
        self.ui.checkBox_7.setDisabled(True)
        self.ui.checkBox_8.setDisabled(True)
        self.ui.checkBox_9.setDisabled(True)
        self.ui.checkBox_10.setDisabled(True)
        self.ui.comboBox.setDisabled(True)
        self.ui.comboBox_3.setDisabled(True)
        self.ui.comboBox_4.setDisabled(True)
        self.ui.comboBox_5.setDisabled(True)
        self.ui.comboBox_6.setDisabled(True)
        self.ui.comboBox_7.setDisabled(True)
        self.ui.comboBox_2.setEnabled(True)
        self.ui.backCaseComboBox.setEnabled(True)
        self.ui.comboBox_2.setEnabled(True)

        #making the checkboxes function
        self.ui.backCaseComboBox.currentIndexChanged.connect(self.updateCheckBox1)
        self.ui.comboBox_2.currentIndexChanged.connect(self.updateCheckBox3)

    def updateCheckBox1(self, index):
        if index > 0:
            self.ui.checkBox_4.setChecked(True)
        else:
            self.ui.checkBox_4.setChecked(False)

    def updateCheckBox3(self, index):
        if index > 0:
            self.ui.checkBox_5.setChecked(True)
        else:
            self.ui.checkBox_5.setChecked(False)

    def SaveNewWorkWorder(self):    
        #using if statements to confirm that all inputs are valid.
        print("today is")
        today = QDate.currentDate()
        print(today)

        if self.ui.backCaseComboBox.currentIndex()<=0 or self.ui.comboBox_2.currentIndex()<=0 or self.ui.createWOCustomerSelection.currentIndex() <=0:
            qtw.QMessageBox.information(self,"Error", "One or more datafields were not selected. Ensure each datafield is complete.")
            return
        
        if self.ui.createWOQuantityInput.value() == 0:
            qtw.QMessageBox.information(self,"Error", "Order quantity must be greater than zero.")
            return

        if not self.ui.createWODeliveryAoFRadioButton.isChecked() and not self.ui.createWODeliveryOtherRadioButton.isChecked() and not self.ui.createWODeliveryPickupRadioButton.isChecked():
            qtw.QMessageBox.information(self,"Error", "Please select a shipping method.")
            return

        if self.ui.createWODateInput.date() < today:
            qtw.QMessageBox.information(self,"Error", "One or more date fields have dates occuring in the past.")
            return
        
        if self.ui.createWORequiredByDate.date() < today:
            qtw.QMessageBox.information(self,"Error", "One or more date fields have dates occuring in the past.")
            return

        if self.ui.createWOProductionDateInput.date() < today :
            qtw.QMessageBox.information(self,"Error", "One or more date fields have dates occuring in the past.")
            return

        else:
            self.ProductTemplateReturn()
            #provide user feedback
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("New Work Order")
            msg_box.setText("New Work Order Completed")
            response = msg_box.exec_()
            if response == qtw.QMessageBox.Ok:   
                self.savedataMethod() #Write data to table
                self.close()  # Close the widget if OK is clicked


    def ProductTemplateReturn(self):
        self.DrillingArrangement = self.ui.comboBox_2.currentText()
        if self.DrillingArrangement == "No drilling":
            self.taskCode = 0
        elif self.DrillingArrangement == "2x back holes":
            self.taskCode = 1
        elif self.DrillingArrangement == "2x front holes":
            self.taskCode = 2
        elif self.DrillingArrangement == "4x holes (2x front + 2x back)":
            self.taskCode = 3


    def savedataMethod(self):
        #****Update the LHS to be the data table save destination
        newWOCustomer = self.ui.createWOCustomerSelection.currentText()
        newWoDate = self.ui.createWODateInput.date()
        newWOQty =  self.ui.createWOQuantityInput.value()
        newWOReqdByDate = self.ui.createWORequiredByDate.date()
        newWOProductionDate = self.ui.createWOProductionDateInput.date()
        newTaskCode = self.taskCode
        newBackCaseSelection = self.ui.backCaseComboBox.currentText()
        newWODeliveryMethod = None
        # I know that there's a better way to do this, but it works. Shows understanding of using the radio button anyway
        if self.ui.createWODeliveryAoFRadioButton.isChecked():
            newWODeliveryMethod = "Address on File"
        if self.ui.createWODeliveryOtherRadioButton.isChecked():
            newWODeliveryMethod = "Other Address"
        if self.ui.createWODeliveryPickupRadioButton.isChecked():
            newWODeliveryMethod = "Customer pickup"

        #confirming that all the fields work - comment this out for final code
        print(newWOCustomer)
        print("WO date")
        print(newWoDate)
        print(newWOQty)
        print("prod date")
        print(newWOProductionDate)
        print("required by")
        print(newWOReqdByDate)
        print(newWODeliveryMethod)
        print(newTaskCode)
        print(newBackCaseSelection)
        print("Today is:")

        

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CreateNewWorkOrderHandler()
    widget.show()
    app.exec()
