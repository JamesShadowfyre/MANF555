from DeleteInventoryWidget import Ui_DeleteInventoryWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QIntValidator  # Import the QIntValidator for numeric validation

class DeleteInventoryHandler(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteInventoryWidget()
        self.ui.setupUi(self)
        self.ui.deleteInventoryButton.clicked.connect(self.deleteInventoryButtonClicked)
# Set QIntValidator to restrict input to integers only
        self.ui.deleteInvItemID.setValidator(QIntValidator())  # Accept any integer value
        self.ui.deleteInvInternalPartID.setValidator(QIntValidator())  # Accept any integer value
        self.ui.deleteInvCost.setValidator(QIntValidator())  # Accept any integer value

    def deleteInventoryButtonClicked(self):
        deleteItemID = self.ui.deleteInvItemID.currentText()
        deleteInternalPartID =  self.ui.deleteInvInternalPartID.text()
        deleteItemName =  self.ui.deleteInvItemName.currentText()
        deleteInvdescription =  self.ui.rdeleteInvDescription.text()
        deleteInventoryCost =  self.ui.deleteInvCost.text()
        deleteInvQtyRecieved =  self.ui.recieveInvQty_2.text()

        print("Deleted Item ID: ")
        print(deleteItemID)
        print("Deleted Item Internal Part ID: ")
        print(deleteInternalPartID)
        print("Deleted Item Name: ")
        print(deleteItemName)
        print("Deleted Item Description: ")
        print(deleteInvdescription)
        print("Deleted Inventory Cost: ")
        print(deleteInventoryCost)
        print("Quantity Deleted: ")
        print(deleteInvQtyRecieved)
        self.close()
        
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = DeleteInventoryHandler()
    widget.show()
    app.exec()