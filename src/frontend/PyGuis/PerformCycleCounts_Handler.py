from frontend.PyGuis.PerformCycleCounts import Ui_updateInventoryWidget
#from PerformCycleCounts import Ui_updateInventoryWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class updateInventoryHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_updateInventoryWidget()
        self.ui.setupUi(self)
        self.ui.updateInventoryCounts.clicked.connect(self.updateInventoryCountsButtonClicked)
# Set QIntValidator to restrict input to integers only
        self.ui.updateInvID.setValidator(QIntValidator())  # Accept any integer value
        self.ui.updateInternalPartID.setValidator(QIntValidator())  # Accept any integer value
        self.ui.updateInvCost.setValidator(QIntValidator())  # Accept any integer value

        self.ui.updateInternalPartID.setDisabled(True)
        self.ui.updateInvName.setDisabled(True)
        self.ui.updateInvDescription.setDisabled(True)
        self.ui.updateInvName.setDisabled(True)
        self.ui.updateInvCost.setDisabled(True)

        # Update the RHS of these entities t o correspond to the table entries
        #-----------------------------------------------------
        # read customer data from table
        # [Item ID, Internal Part ID, Item Name, Item Description, Item Cost, Item Qty] all strings
        # I've assumed COST is FLOAT
        #-----------------------------------------------------
        self.userData = [["0001", "321798", "Back Case - Black", "Back Case - Black", "10", 11], ["0002", "90639", "Back Case - Blue", "Back Case - Blue", "10", 12]]
        IDs = [item[0] for item in self.userData]

        self.refreshEditCustomerData()
        self.ui.updateInvID.clear()
        self.ui.updateInvID.addItems(IDs)
        self.ui.updateInvName.addItems(["-","Back Case - Black","Back Case - Blue", "Back Case - Red"])
        self.ui.updateInvID.currentIndexChanged.connect(self.refreshEditCustomerData)

        #set default visibilities
        self.ui.updateInvDescription.setDisabled(True)
        self.ui.updateInvCost.setDisabled(True)


    def refreshEditCustomerData(self):

        selectedCustomerID = self.ui.updateInvID.currentText()
        
        # Find matching user data from self.userData
        matching_item = next((item for item in self.userData if item[0] == selectedCustomerID), None)
        
        # If a matching customer is found, populate the UI fields
        if matching_item:
            self.ui.updateInternalPartID.setText(matching_item[1])  
            self.ui.updateInvName.setCurrentText(matching_item[2])  
            self.ui.updateInvDescription.setText(matching_item[3])  
            self.ui.updateInvCost.setText(str(matching_item[4])) 
            self.ui.updateInvQtyRecieved.setValue(matching_item[5])
        else:
            # Clear all fields if no matching item is found
            self.ui.updateInternalPartID.clear()
            self.ui.updateInvName.clear()
            self.ui.updateInvDescription.clear()
            self.ui.updateInvCost.clear()
            print("No matching item found")

    def updateInventoryCountsButtonClicked(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Perform Cycle Count")
        msg_box.setText("Are you sure you want to perform a cycle count? This action cannot be undone.")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.saveCustomerDataEditMethod()
            self.close()  # Close the widget if OK is clicked
            #Code to modify the entry from the database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked
        
        # updateItemID = self.ui.updateInvID.currentText()
        # updateInternalPartID =  self.ui.updateInternalPartID.text()
        # updateItemName =  self.ui.updateInvName.currentText()
        # updateInvdescription =  self.ui.updateInvDescription.text()
        # updateInventoryCost =  self.ui.updateInvCost.text()
        # updateInvQtyRecieved =  self.ui.updateInvQtyRecieved.text()

        # print("Updated Item ID: ",updateItemID)
        # print("Updated Item Internal Part ID: ",updateInternalPartID)
        # print("Updated Item Name: ",updateItemName)
        # print("Updated Item Description: ",updateInvdescription)
        # print("Updated Item Cost: ",updateInventoryCost)
        # print("Quantity Recieved: ",updateInvQtyRecieved)
        # self.close()


    def saveCustomerDataEditMethod(self):
        #write data to database
        #Update the LHS to match the database write columns
        field = ["","","","","",""]
        field[0] = self.ui.updateInvID.currentText()
        field[1] = self.ui.updateInternalPartID.text()
        field[2] = self.ui.updateInvName.currentText()
        field[3] = self.ui.updateInvDescription.text()    
        field[4] = float(self.ui.updateInvCost.text()) 
        field[5] = self.ui.updateInvQtyRecieved.value()

        print(field)

        # Update the RHS of these entities to correspond to the table entries
        #-----------------------------------------------------
        # wrote field to table
        # [Item ID, Internal Part ID, Item Name, Item Description, Item Cost, Item Qty] [string, string string string, string, int]
        # I've assumed COST is FLOAT
        #-----------------------------------------------------

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = updateInventoryHandler()
    widget.show()
    app.exec()