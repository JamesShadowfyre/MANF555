from CreateNewInventory import Ui_createNewInventorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class CreateNewInventoryHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_createNewInventorWidget()
        self.ui.setupUi(self)
        self.ui.newInventorySaveButton.clicked.connect(self.newInventorySaveButtonClicked)
# Set QIntValidator to restrict input to integers only
        self.ui.newInvInternalPartID.setValidator(QIntValidator())  # Accept any integer value
        self.ui.newInvItemCost.setValidator(QIntValidator())  # Accept any integer value
        self.ui.newInvItemQty.setValidator(QIntValidator())  # Accept any integer value

    def newInventorySaveButtonClicked(self):
        newItemName = self.ui.newInvItemName.text()
        newInvInternalPartID =  self.ui.newInvInternalPartID.text()
        newInvItemDescription =  self.ui.newInvItemDescription.text()
        newInvItemCost =  self.ui.newInvItemCost.text()
        newInvItemQty =  self.ui.newInvItemQty.text()

        print("New Item Name: ")
        print(newItemName)
        print("New Item Internal Part ID: ")
        print(newInvInternalPartID)
        print("New Item Description: ")
        print(newInvItemDescription)
        print("New Item Cost: ")
        print(newInvItemCost)
        print("New Item Quantity: ")
        print(newInvItemQty)
        self.close()

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CreateNewInventoryHandler()
    widget.show()
    app.exec()