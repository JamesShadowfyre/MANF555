from frontend.PyGuis.CreateNewInventory import Ui_createNewInventorWidget
#from CreateNewInventory import Ui_createNewInventorWidget
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
        field = ["","","","",""]

        field[0] =  self.ui.newInvInternalPartID.text()
        field[1] = self.ui.newInvItemName.text()
        field[2] =  self.ui.newInvItemDescription.text()
        field[3] =  float(self.ui.newInvItemCost.text())
        field[4] =  self.ui.newInvItemQty.text()


  #-----------------------------------------------------
        #James: 
        # write field to database - note that this one doesn't have the account ID as the 0th element!
        #[Part ID, Part Name, Part Description, Cost, Qty] assuming cost is a float
  #-----------------------------------------------------

        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CreateNewInventoryHandler()
    widget.show()
    app.exec()