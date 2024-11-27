#Create Work Order Widget Handler

"""
Remaining work:
- Update local variables to use database table connections
- Not sure what trigger to use to get the checkbox to change... should probably just delete this feature
"""

from CreateWorkOrderWidgetrev4 import Ui_CreateWorkOrderWidget

from PyQt5 import QtWidgets as qtw

class CreateNewWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        self.ui.createWOCustomerSelection.addItems(["Steve", "Bob", "Joe"]) #change this with actual items from table
        self.ui.comboBox_2.addItems(["", "No drilling", "2x back holes", "2x front holes", "4x holes (2x front + 2x back)"])
        self.ui.backCaseComboBox.addItems(["","Black"])

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
        #qtw.QMessageBox.information(self, "New Work Order", "New Work Order Saved")
        
        if self.ui.backCaseComboBox.currentIndex() <= 0 or self.ui.comboBox_2.currentIndex() <= 0:
            print("A box was not selected")
            qtw.QMessageBox.information(self,"Error", "One or more datafields were not selected. Ensure each datafield is complete.")
        
        else:
            self.DrillingArrangement = self.ui.comboBox_2.currentText()
            self.BackCaseSelection = self.ui.backCaseComboBox.currentText()
            self.ProductTemplateReturn()
            self.close()
        
        
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("New Work Order")
        msg_box.setText("New Work Order Completed")
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:  
            self.savedataMethod()
            self.close()  # Close the widget if OK is clicked


    def ProductTemplateReturn(self):

        if self.DrillingArrangement == "No drilling":
            self.taskCode = 0
        elif self.DrillingArrangement == "2x back holes":
            self.taskCode = 1
        elif self.DrillingArrangement == "2x front holes":
            self.taskCode = 2
        elif self.DrillingArrangement == "4x holes (2x front + 2x back)":
            self.taskCode = 3
               

    def savedataMethod(self):
        newWOCustomer = self.ui.createWOCustomerSelection.currentText()
        newWoDate = self.ui.createWODateInput.date()
        newWOQty =  self.ui.createWOQuantityInput.value()
        newWOReqdByDate = self.ui.createWORequiredByDate.date()
        newWOProductionDate = self.ui.createWOProductionDateInput.date()
        newTaskCode = self.taskCode
        newBackCaseSelection = self.ui.backCaseComboBox

        # I know that there's a better way to do this, but it works. Shows understanding of using the radio button anyway
        if self.ui.createWODeliveryAoFRadioButton.isChecked():
            newWODeliveryMethod = "Address on File"
        if self.ui.createWODeliveryOtherRadioButton.isChecked():
            newWODeliveryMethod = "Other Address"
        if self.ui.createWODeliveryPickupRadioButton.isChecked():
            newWODeliveryMethod = "Customer pickup"

        #A new WO number will need to be created, this can be done by the table or adding 1 to the largest WO number in the system.

        print(newWOCustomer)
        print(newWoDate)
        print(newWOQty)
        print(newWOReqdByDate)
        print(newWOProductionDate)
        print(newWODeliveryMethod)
        print(newTaskCode)
        print(newBackCaseSelection)

        pass

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CreateNewWorkOrderHandler()
    widget.show()
    app.exec()
