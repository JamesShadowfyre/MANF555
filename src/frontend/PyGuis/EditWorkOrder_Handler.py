#Edit Work Order Handler

"""
Remaining work:
- Update local variables to use database table connections
- Not sure what trigger to use to get the checkbox to change... should probably just delete this feature
- need to get the error trapping working better for checking for valid inputs on the date functions, and the check for the 0 qty. Qspin Box to int conversion?
"""

from EditWorkOrderWidget import Ui_CreateWorkOrderWidget
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore

class EditWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        
        #set all of these equal to database values
        list = ["","1","2","3","4"]
        self.ui.WorkOrderNumber.addItems(list)
        
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
        
        customerfromTable = "string1"
        WODatefromTable = "string2"
        QtyfromTable = "string3"
        woProddatefromTable  ="string4"
        woreqdatefromTable = "string5"
        shipmethodfromTable = "string6"
        backCasefromTable = "string7"

        self.ui.createWOCustomerSelection.setText(customerfromTable)
        self.ui.createWODateInput.setText(WODatefromTable)
        self.ui.createWOQuantityInput.setText(QtyfromTable)
        self.ui.createWOProductionDateInput.setText(woProddatefromTable)
        self.ui.createWORequiredByDate.setText(woreqdatefromTable)
        self.ui.lineEdit_6.setText(shipmethodfromTable)
        self.ui.backCaseComboBox.setText(backCasefromTable)

#Enable the entire UI except the "select WO combobox"
        self.ui.lineEdit.setDisabled(False)
        self.ui.lineEdit_2.setDisabled(False)
        self.ui.lineEdit_3.setDisabled(False)
        self.ui.lineEdit_4.setDisabled(False)
        self.ui.lineEdit_5.setDisabled(False)
        self.ui.lineEdit_7.setDisabled(False)
        self.ui.comboBox_2.setEnabled(False)
        self.ui.backCaseComboBox.setEnabled(False)
        self.ui.backCaseComboBox.setDisabled(False)
        self.ui.createWOCustomerSelection.setDisabled(False)
        self.ui.createWODateInput.setDisabled(False)
        self.ui.createWOProductionDateInput.setDisabled(False)
        self.ui.createWOQuantityInput.setDisabled(False)
        self.ui.createWORequiredByDate.setDisabled(False)
        self.ui.lineEdit_6.setDisabled(False)
        self.ui.comboBox_2.setDisabled(False)

    def SaveNewWorkWorder(self, taskcodeValue):    
        #using if statements to confirm that all inputs are valid.

            self.ProductTemplateReturn(taskcodeValue)
            
            #provide user feedback
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("Save Changes")
            msg_box.setText("Are you sure you wish to save changes? This action cannot be undone")
            response = msg_box.exec_()
            if response == qtw.QMessageBox.Ok:   
                self.savedataMethod(taskcodeValue) #Write data to table
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
        
    def savedataMethod(self,taskcodeValue):
        #****Update the LHS to be the data table save destination
        datatablevalue = taskcodeValue
        print("Edits saved.")

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditWorkOrderHandler()
    widget.show()
    app.exec()
