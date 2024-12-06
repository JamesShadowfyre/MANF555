#Recieve Inventory Widget Handler
from frontend.PyGuis.RecieveInventoryWidget import Ui_recieveInventoryWidget
#from RecieveInventoryWidget import Ui_recieveInventoryWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class RecieveInventoryWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_recieveInventoryWidget()
        self.ui.setupUi(self)

        # Initially disable fields
        self.ui.recieveInvDescription.setDisabled(True)
        self.ui.recieveInvCost.setDisabled(True)
        self.ui.recieveInvItemName.setDisabled(True)
        self.ui.recieveInvQty.setDisabled(True)
        self.ui.recieveInvInternalPartID.setDisabled(True)

        #-----------------------------------------------------
        #James: 
        # read self.invData_all field as SQL query with the below columns in the order stated:
        ##["Internal Part ID", "Quantity", "Name", "Description", "Unit Cost ($)"] assuming cost is a float
  #-----------------------------------------------------

        self.invData = [["0111", 5, "Back Cover", "Black", 1],["0222", 6, "Back Cover", "Blue", "11"]]
        invIDs = [item[0] for item in self.invData]
        # Connect Item ID selection to autofill function
        self.ui.recieveInvItemID.addItems(invIDs) 

        self.ui.recieveInvItemID.currentIndexChanged.connect(self.on_selection_change)
        self.ui.recieveInvItemID.currentTextChanged.connect(self.autofillFields)

        # Connect Save button to save function
        self.ui.recieveInventorySaveButton.clicked.connect(self.receiveInventorySaveButtonClicked)
        self.ui.recieveInvQty.setDisabled(True)
        # Disable fields initially
        self.disableFields()
        self.autofillFields()


    def disableFields(self):
        self.ui.recieveInvInternalPartID.setDisabled(True)
        self.ui.recieveInvItemName.setDisabled(True)
        self.ui.recieveInvDescription.setDisabled(True)
        self.ui.recieveInvCost.setDisabled(True)

    def autofillFields(self):
        # Get the selected Item ID
        selectedItemID = self.ui.recieveInvItemID.currentText()

        #Find matching user data from self.userData
        matching_inv = next((item for item in self.invData if item[0] == selectedItemID), None)
        
        # If a matching customer is found, populate the UI fields
        if matching_inv:
            self.ui.recieveInvInternalPartID.setText(matching_inv[0])
            self.ui.recieveInvItemName.setText(matching_inv[2])  # Inv part Name
            self.ui.recieveInvDescription.setText(matching_inv[3])  # Description
            self.ui.recieveInvCost.setText(str(matching_inv[4]))  # cost
            # Enable the fields after autofilling
            self.enableFields()
        else:
            # Clear and disable fields if no valid selection
            self.clearFields()
            self.disableFields()

        self.disableFields()

    def enableFields(self):
        self.ui.recieveInvInternalPartID.setEnabled(True)
        self.ui.recieveInvItemName.setEnabled(True)
        self.ui.recieveInvDescription.setEnabled(True)
        self.ui.recieveInvCost.setEnabled(True)
        self.ui.recieveInvQty.setEnabled(True)

    def clearFields(self):
        self.ui.recieveInvItemID.clear()
        self.ui.recieveInvInternalPartID.clear()
        self.ui.recieveInvItemName.clear()
        self.ui.recieveInvDescription.clear()
        self.ui.recieveInvCost.clear()
        self.ui.recieveInvQty.clear()

    def on_selection_change(self, index):
        if index != -1:
            print(f"Item selected: {self.ui.recieveInvItemID.currentText()}")
        else:
            print("No item selected.")

    def receiveInventorySaveButtonClicked(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Receive Inventory")
        msg_box.setText("Click OK to receive the shipment to inventory")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()

        if response == qtw.QMessageBox.Ok:

            field = ["",0,"","",0] #initialize
            field[0] = self.ui.recieveInvInternalPartID.text()
            field[1] = int(self.ui.recieveInvQty.value())
            field[2] = self.ui.recieveInvItemName.text()
            field[3] = self.ui.recieveInvDescription.text()
            field[4] = float(self.ui.recieveInvCost.text())


        #-----------------------------------------------------
        #James: 
        # write field to database - note that this one doesn't have the account ID as the 0th element!
        ##["Internal Part ID", "Quantity", "Name", "Description", "Unit Cost ($)"] assuming cost is a float, qty as int
        #-----------------------------------------------------



            self.close()  # Close the widget if OK is clicked
            # Code to update database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked
        
 


       
        # self.close()



if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = RecieveInventoryWidgetHandler()
    widget.show()
    app.exec()
