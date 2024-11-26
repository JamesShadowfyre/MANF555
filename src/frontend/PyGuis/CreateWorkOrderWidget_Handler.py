#Create Work Order Widget Handler

"""
Remaining work:
- Update local variables to use database table connections
- Not sure what trigger to use to get the checkbox to change... should probably just delete this feature
"""
import ProductTemplate_Handler
from CreateWorkOrderWidget import Ui_CreateWorkOrderWidget

from PyQt5 import QtWidgets as qtw

class CreateNewWorkOrderHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_CreateWorkOrderWidget()
        self.ui.setupUi(self)
        self.ui.createWOCustomerSelection.addItems(["Steve", "Bob", "Joe"]) #change this with actual items from table
        self.ui.checkBox.setDisabled(True)

        self.ui.createNewWOSaveButton.clicked.connect(self.SaveNewWorkWorder)
        self.ui.productTemplateViewButton.clicked.connect(self.ProductTemplateButtonAction)

        
    def SaveNewWorkWorder(self):    
        #qtw.QMessageBox.information(self, "New Work Order", "New Work Order Saved")
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("New Work Order")
        msg_box.setText("New Work Order Completed")
        response = msg_box.exec_()
        if response == qtw.QMessageBox.Ok:
            self.savedataMethod()
            self.close()  # Close the widget if OK is clicked

    def ProductTemplateButtonAction(self):
        print("Button pressed")
        self.productTemplateWidget = ProductTemplate_Handler.ProductTemplateHandler()
        self.productTemplateWidget.show()
        
    def savedataMethod(self):
        newWOCustomer = self.ui.createWOCustomerSelection.currentText()
        newWoDate = self.ui.createWODateInput.date()
        newWOQty =  self.ui.createWOQuantityInput.value()
        newWOReqdByDate = self.ui.createWORequiredByDate.date()
        newWOProductionDate = self.ui.createWOProductionDateInput.date()
        newTaskCode = self.productTemplateWidget.taskCode #passing from the pop-up widget back to this screen
        newBackCaseSelection  = self.productTemplateWidget.BackCaseSelection #passing from the pop-up widget back to this screen

        # I know that there's a better way to do this, but it works. Shows understanding of using the radio button anyway
        if self.ui.createWODeliveryAoFRadioButton.isChecked():
            newWODeliveryMethod = "Address on File"
        if self.ui.createWODeliveryOtherRadioButton.isChecked():
            newWODeliveryMethod = "Other Address"
        if self.ui.createWODeliveryPickupRadioButton.isChecked():
            newWODeliveryMethod = "Customer pickup"

        #A new WO number will need to be created, this can be done by the table or adding 1 to the largest WO number in the system.

        print(newWOCustomer)
        print(newWoDate)
        print(newWOQty)
        print(newWOReqdByDate)
        print(newWOProductionDate)
        print(newWODeliveryMethod)
        print(newTaskCode)
        print(newBackCaseSelection)

        pass

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CreateNewWorkOrderHandler()
    widget.show()
    app.exec()
