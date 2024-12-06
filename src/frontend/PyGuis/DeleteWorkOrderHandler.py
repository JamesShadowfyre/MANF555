#Delete Work Order handler

#Create Work Order Widget Handler

"""
Remaining work:
- Update local variables to use database table connections
- Not sure what trigger to use to get the checkbox to change... should probably just delete this feature
- need to get the error trapping working better for checking for valid inputs on the date functions, and the check for the 0 qty. Qspin Box to int conversion?
"""

from frontend.PyGuis.DeleteWorkOrderRev4 import Ui_CreateWorkOrderWidget
from backend.apiAccessPoint import ApplicationHome
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore

class DeleteWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        
        #set all of these equal to database values
        api = ApplicationHome()
        self.WOs = api.getWorkOrderList()
        list =  self.WOs.keys()
        self.ui.WorkOrderNumber.addItems(map(str, list))
        
        self.ui.createWOCustomerSelection.setText("")
        self.ui.createWODateInput.setText("")
        self.ui.createWOQuantityInput.setText("")
        self.ui.createWOProductionDateInput.setText("")
        self.ui.createWORequiredByDate.setText("")
        self.ui.lineEdit_6.setText("")
        self.ui.backCaseComboBox.setText("")
        
        taskcodeValue = 1 #set to taskCode from database - James

        self.ProductTemplateReturn(taskcodeValue)

        
        self.ui.createNewWOSaveButton.clicked.connect(self.SaveNewWorkWorder)

#Disable the entire UI except the "select WO combobox"
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

    def updateUI(self, taskcodeValue):
     
        #use taskCodeValue to search for other elements from the database to update UI
        self.ProductTemplateReturn(2)

        chosenWO = self.WOs.get(int(taskcodeValue))
        customerfromTable = chosenWO.getCustomer()
        WODatefromTable = ""
        QtyfromTable = str(chosenWO.getQuantity())
        woProddatefromTable  =""
        woreqdatefromTable = ""
        shipmethodfromTable = ""
        items = list(chosenWO.getComponent().keys())
        try:
            backCasefromTable = items[0]
        except:
            backCasefromTable = ""

        self.ui.createWOCustomerSelection.setText(customerfromTable)
        self.ui.createWODateInput.setText(WODatefromTable)
        self.ui.createWOQuantityInput.setText(QtyfromTable)
        self.ui.createWOProductionDateInput.setText(woProddatefromTable)
        self.ui.createWORequiredByDate.setText(woreqdatefromTable)
        self.ui.lineEdit_6.setText(shipmethodfromTable)
        self.ui.backCaseComboBox.setText(backCasefromTable)

    def SaveNewWorkWorder(self, taskcodeValue):    
        #using if statements to confirm that all inputs are valid.

            self.ProductTemplateReturn(taskcodeValue)
            #provide user feedback
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("Delete Work Order")
            msg_box.setText("Are you sure you wish to delete the work order?")
            response = msg_box.exec_()
            if response == qtw.QMessageBox.Ok:   
                self.savedataMethod(self.ui.WorkOrderNumber.currentText()) #Write data to table
                self.close()  # Close the widget if OK is clicked


    def ProductTemplateReturn(self, taskcodeValue):
        #initialize
        self.taskCode = taskcodeValue
        
        if self.taskCode == 0 :
             self.ui.comboBox_2.setText("No drilling")
        elif self.taskCode == 1:
            self.ui.comboBox_2.setText("2x back holes")
        elif self.taskCode == 2:
            self.ui.comboBox_2.setText("2x front holes")
        elif self.taskCode == 3:
            self.ui.comboBox_2.setText("4x holes (2x front + 2x back)")

        taskcodeValue = self.taskCode
        
    def savedataMethod(self,woNumber):
        #****Update the LHS to be the data table save destination
        api = ApplicationHome()
        api.setWorkOrderFunctions('delete',id=woNumber)

        print("Data deleted")

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = DeleteWorkOrderHandler()
    widget.show()
    app.exec()
