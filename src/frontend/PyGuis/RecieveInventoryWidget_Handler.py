#Recieve Inventory Widget Handler


from frontend.PyGuis.RecieveInventoryWidget import Ui_recieveInventoryWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class RecieveInventoryWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_recieveInventoryWidget()
        self.ui.setupUi(self)

        self.ui.recieveInvDescription.setDisabled(True)
        self.ui.recieveInvCost.setDisabled(True)
        self.ui.recieveInvItemName.setDisabled(True)
        self.ui.recieveInvQty.setDisabled(True)
        self.ui.recieveInvInternalPartID.setDisabled(True)
        self.ui.recieveInvItemID.currentIndexChanged.connect(self.on_selection_change)
        self.ui.recieveInvItemID.addItems(["----", "0001", "0002", "0003"]) #replace with connection to inventory table
        
        self.ui.recieveInventorySaveButton.clicked.connect(self.receiveInventorySaveButtonClicked)



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
            self.close()  # Close the widget if OK is clicked
            #Code to update database
        elif response == qtw.QMessageBox.Cancel:
            pass  # Do nothing if Cancel is clicked

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = RecieveInventoryWidgetHandler()
    widget.show()
    app.exec()
