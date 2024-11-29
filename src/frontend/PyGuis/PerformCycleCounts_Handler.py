from PerformCycleCounts import Ui_updateInventoryWidget
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


    def updateInventoryCountsButtonClicked(self):
        updateItemID = self.ui.updateInvID.currentText()
        updateInternalPartID =  self.ui.updateInternalPartID.text()
        updateItemName =  self.ui.updateInvName.currentText()
        updateInvdescription =  self.ui.updateInvDescription.text()
        updateInventoryCost =  self.ui.updateInvCost.text()
        updateInvQtyRecieved =  self.ui.updateInvQtyRecieved.text()

        print("Updated Item ID: ")
        print(updateItemID)
        print("Updated Item Internal Part ID: ")
        print(updateInternalPartID)
        print("Updated Item Name: ")
        print(updateItemName)
        print("Updated Item Description: ")
        print(updateInvdescription)
        print("Updated Item Cost: ")
        print(updateInventoryCost)
        print("Quantity Recieved: ")
        print(updateInvQtyRecieved)
        self.close()

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = updateInventoryHandler()
    widget.show()
    app.exec()