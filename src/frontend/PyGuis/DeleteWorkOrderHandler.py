#Delete Work Order handler

#Create Work Order Widget Handler

"""
Remaining work:
- Update local variables to use database table connections
- Not sure what trigger to use to get the checkbox to change... should probably just delete this feature
- need to get the error trapping working better for checking for valid inputs on the date functions, and the check for the 0 qty. Qspin Box to int conversion?
"""

from DeleteWorkOrderRev4 import Ui_CreateWorkOrderWidget
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore

class DeleteWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        
        #setting the text of the boxes = the WO selected
        self.ui.WorkOrderNumber.addItems(["","1","2","3","4"])
        self.ui.createWODateInput.setText("hello")
        self.ui.createWOQuantityInput.setText("hello")
        self.ui.createWORequiredByDate.setText("hello")
        self.ui.createWOProductionDateInput.setText("hello")
        self.ui.backCaseComboBox.setText("hello")
        self.ui.lineEdit_6.setText("hello")
        taskcode = 1

        #Disable the entire UI except the "select WO combobox"
        self.ui.createNewWOSaveButton.clicked.connect(self.SaveNewWorkWorder)

        self.ui.lineEdit.setDisabled(True)
        self.ui.lineEdit_2.setDisabled(True)
        self.ui.lineEdit_3.setDisabled(True)
        self.ui.lineEdit_4.setDisabled(True)
        self.ui.lineEdit_5.setDisabled(True)
        self.ui.lineEdit_7.setDisabled(True)
        self.ui.comboBox_2.setEnabled(True)
        self.ui.backCaseComboBox.setEnabled(True)
        self.ui.backCaseComboBox.setDisabled(True)
        self.ui.createWOCustomerSelection.setDisabled(True)
        self.ui.createWODateInput.setDisabled(True)
        self.ui.createWOProductionDateInput.setDisabled(True)
        self.ui.createWOQuantityInput.setDisabled(True)
        self.ui.createWORequiredByDate.setDisabled(True)
        self.ui.lineEdit_6.setDisabled(True)
        self.ui.comboBox_2.setDisabled(True)

        self.ui.WorkOrderNumber.currentTextChanged.connect(self.updateUI)

    def updateUI(self):
        pass

    def SaveNewWorkWorder(self):    
        #using if statements to confirm that all inputs are valid.

            self.ProductTemplateReturn()
            #provide user feedback
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("Delete Work Order")
            msg_box.setText("Are you sure you wish to delete the work order?")
            response = msg_box.exec_()
            if response == qtw.QMessageBox.Ok:   
                self.savedataMethod() #Write data to table
                self.close()  # Close the widget if OK is clicked


    def ProductTemplateReturn(self, taskcode):
        
        #initialize
        self.DrillingArrangement = self.ui.comboBox_2.currentText()

        if self.taskCode == 0 :
             self.DrillingArrangement = "No drilling"
        elif self.taskCode == 1:
            self.DrillingArrangement = "2x back holes"
        elif self.taskCode == 2:
            self.DrillingArrangement = "2x front holes"
        elif self.taskCode == 3:
            self.DrillingArrangement == "4x holes (2x front + 2x back)"
            

        self.DrillingArrangement = self.ui.comboBox_2.currentText()


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


        #confirming that all the fields work - comment this out for final code
        #print(newWOCustomer)
        #print("WO date")
        #print(newWoDate)
        #print(newWOQty)
        #print("prod date")
        #print(newWOProductionDate)
        #print("required by")
        #print(newWOReqdByDate)
        #print(newWODeliveryMethod)
        #print(newTaskCode)
        #print(newBackCaseSelection)
        #print("Today is:")

        

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = DeleteWorkOrderHandler()
    widget.show()
    app.exec()
