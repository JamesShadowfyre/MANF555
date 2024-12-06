#Edit Work Order Handler

"""
Remaining work:
- Update local variables to use database table connections
- There is some problem as to why the taskcode isn't updating when saving the userData
- I am getting really confused looking at this. Moving onto something else. 
"""

from frontend.PyGuis.EditWorkOrderWidget import Ui_CreateWorkOrderWidget
#from EditWorkOrderWidget import Ui_CreateWorkOrderWidget
from PyQt5.QtCore import QDate
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore

class EditWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        
        #-----------------------------------------------------
        #Read list of all WO IDs and Customer Account IDs from tables
        #Then read the list of work order information
        #-----------------------------------------------------    
        list = ["","1","2","3","4"] #WO number - update with sql data
        customers = ["cust1", "cust2", "cust3"] # acct idupdate with sql data

        WOInfo = []

        self.ui.WorkOrderNumber.addItems(list)
        self.ui.comboBox_3.addItems(customers)
        self.ui.createWODateInput.setText("")
        self.ui.createWOQuantityInput.setText("")
        self.ui.createWOProductionDateInput.setText("")
        self.ui.createWORequiredByDate.setText("")
        self.ui.comboBox.setCurrentText("")
        self.ui.comboBox_2.setCurrentText("")
        self.ui.comboBox_4.setCurrentText("")
        
        taskcodeValue = None #set to taskCode from database - James

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
        self.ui.comboBox_2.setEnabled(True)
        self.ui.comboBox_4.setDisabled(True)
        self.ui.comboBox_2.setDisabled(True)
        self.ui.createWODateInput.setDisabled(True)
        self.ui.createWOProductionDateInput.setDisabled(True)
        self.ui.createWOQuantityInput.setDisabled(True)
        self.ui.createWORequiredByDate.setDisabled(True)
        self.ui.comboBox_3.setDisabled(True)
        self.ui.comboBox_2.setDisabled(True)
        self.ui.comboBox.setDisabled(True)

        self.ui.WorkOrderNumber.currentTextChanged.connect(self.updateUI)

    def updateUI(self, taskcodeValue):
     
        #use taskCodeValue to search for other elements from the database to update UI
        #Update the RHS of the arguments to the table entries
        self.ProductTemplateReturn(taskcodeValue)
        
        customerfromTable = "string1"
        WODatefromTable = "string2"
        QtyfromTable = "string3"
        woProddatefromTable  ="string4"
        woreqdatefromTable = "string5"
        shipmethodfromTable = "string6"
        backCasefromTable = "string7"

        self.ui.comboBox_3.setCurrentText(customerfromTable)
        self.ui.createWODateInput.setText(WODatefromTable)
        self.ui.createWOQuantityInput.setText(QtyfromTable)
        self.ui.createWOProductionDateInput.setText(woProddatefromTable)
        self.ui.createWORequiredByDate.setText(woreqdatefromTable)
        self.ui.comboBox.setCurrentText(shipmethodfromTable)
        self.ui.comboBox_2.setCurrentText(backCasefromTable)

#Enable the entire UI except the "select WO combobox"

        self.ui.comboBox_4.setDisabled(False)
        self.ui.comboBox.setDisabled(False)
        self.ui.createWODateInput.setDisabled(False)
        self.ui.createWOProductionDateInput.setDisabled(False)
        self.ui.createWOQuantityInput.setDisabled(False)
        self.ui.createWORequiredByDate.setDisabled(False)
        self.ui.comboBox_2.setDisabled(False)
        self.ui.comboBox_3.setDisabled(False)

    def SaveNewWorkWorder(self, taskcodeValue):    

        self.ProductTemplateReturn(taskcodeValue)
        
        #provide user feedback
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Save Changes")
        msg_box.setText("Are you sure you wish to save changes? This action cannot be undone")
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:   
            
            userData = ["","","","","","","",0]
            
            userData[0] = self.ui.comboBox_3.currentText() #customerfromTable
            userData[1] =self.ui.createWODateInput.text()#WODatefromTable
            userData[2] =self.ui.createWOQuantityInput.text() #QtyfromTable
            userData[3] =self.ui.createWOProductionDateInput.text() #woProddatefromTable
            userData[4] =self.ui.createWORequiredByDate.text() #woreqdatefromTable
            userData[5] =self.ui.comboBox.currentText() #shipmethodfromTable
            userData[6] =self.ui.comboBox_2.currentText() #backCasefromTable

            taskcodeinput = self.ui.comboBox_4.currentText()
            print(taskcodeinput)

            #convert task code to 0 to 3 measure
            if taskcodeinput == "No Drilling":
                userData[7] = 0
            if taskcodeinput == "2x back holes":
                userData[7] = 1
            if taskcodeinput == "2x front holes":
                userData[7] = 2
            if taskcodeinput == "4x holes (2x front + 2x back)":
                userData[7] = 3

            print(userData)

            #-----------------------------------------------------
            #write userData to database
            #[Customer Acct ID, Username, rights, password] - rights is boolean, the rest are strings
            #-----------------------------------------------------    
            self.close()  # Close the widget if OK is clicked


    def ProductTemplateReturn(self, taskcodeValue):
        #initialize
        self.taskCode = taskcodeValue
        
        if self.taskCode == 0 :
             self.ui.comboBox_4.setCurrentText("No drilling")
        elif self.taskCode == 1:
            self.ui.comboBox_4.setCurrentText("2x back holes")
        elif self.taskCode == 2:
            self.ui.comboBox_4.setCurrentText("2x front holes")
        elif self.taskCode == 3:
            self.ui.comboBox_4.setCurrentText("4x holes (2x front + 2x back)")
        elif self.taskCode == None:
            self.ui.comboBox_4.setCurrentText("")

        taskcodeValue = self.taskCode
        
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = EditWorkOrderHandler()
    widget.show()
    app.exec()
