#Recieve Inventory Widget Handler
from frontend.PyGuis.RecieveInventoryWidget import Ui_recieveInventoryWidget
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

        # Connect Item ID selection to autofill function
        self.ui.recieveInvItemID.addItems(["----", "0001", "0002", "0003"])  # Replace with real items
        self.ui.recieveInvItemID.currentIndexChanged.connect(self.on_selection_change)
        self.ui.recieveInvItemID.currentTextChanged.connect(self.autofillFields)

        # Connect Save button to save function
        self.ui.recieveInventorySaveButton.clicked.connect(self.receiveInventorySaveButtonClicked)

        # Mock data to simulate fetching from a database
        self.selectItemID = {
            "0001": {
                "internalPartID": "95317",
                "inventoryItemName": "Back Case - Black",
                "invetoryDescription": "Back Case - Black",
                "inventoryCost": "10",
                "quantity": "20"
            },
            "0002": {
                "internalPartID": "95318",
                "inventoryItemName": "Back Case - Blue",
                "invetoryDescription": "Back Case - Blue",
                "inventoryCost": "10",
                "quantity": "15"
            },
            "0003": {
                "internalPartID": "95319",
                "inventoryItemName": "Back Case - Red",
                "invetoryDescription": "Back Case - Red",
                "inventoryCost": "10",
                "quantity": "30"
            }
        }

        # Item Names for ComboBox
        self.itemName = ["", "Back Case - Black", "Back Case - Blue", "Back Case - Red"]
        self.ui.recieveInvItemName.addItems(self.itemName)

        # Disable fields initially
        self.disableFields()

    def disableFields(self):
        self.ui.recieveInvInternalPartID.setDisabled(True)
        self.ui.recieveInvItemName.setDisabled(True)
        self.ui.recieveInvDescription.setDisabled(True)
        self.ui.recieveInvCost.setDisabled(True)
        self.ui.recieveInvQty.setDisabled(True)

    def autofillFields(self):
        # Get the selected Item ID
        ItemIDCode = self.ui.recieveInvItemID.currentText()

        # If a valid item ID is selected and it's not empty
        if ItemIDCode and ItemIDCode in self.selectItemID:
            # Get corresponding data for the item
            data = self.selectItemID[ItemIDCode]

            # Autofill fields
            self.ui.recieveInvInternalPartID.setText(data["internalPartID"])
            self.ui.recieveInvItemName.setCurrentText(data["inventoryItemName"])  # Use setCurrentText for comboboxes
            self.ui.recieveInvDescription.setText(data["invetoryDescription"])
            self.ui.recieveInvCost.setText(data["inventoryCost"])
            self.ui.recieveInvQty.setValue(int(data["quantity"]))  # Use setValue for spinboxes

            # Enable the fields after autofilling
            self.enableFields()
        else:
            # Clear and disable fields if no valid selection
            self.clearFields()
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
        inventoryItemID = self.ui.recieveInvItemID.currentText()
        internalPartID = self.ui.recieveInvInternalPartID.text()
        inventoryItemName = self.ui.recieveInvItemName.currentText()
        invetoryDescription = self.ui.recieveInvDescription.text()
        inventoryCost = self.ui.recieveInvCost.text()
        quantity = self.ui.recieveInvQty.text()

        print("Following item(s) recieved: ")
        print("Item ID: ", inventoryItemID)
        print("Internal Part ID: ", internalPartID)
        print("Item Name: ", inventoryItemName)
        print("Item Description: ", invetoryDescription)
        print("Item Cost: ", inventoryCost)
        print("Quantity Recieved: ", quantity)
        # self.close()

        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Receive Inventory")
        msg_box.setText("Click OK to receive the shipment to inventory")
        msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        response = msg_box.exec_()

        if response == qtw.QMessageBox.Ok:
            self.close()  # Close the widget if OK is clicked
            # Code to update database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = RecieveInventoryWidgetHandler()
    widget.show()
    app.exec()
