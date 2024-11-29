from ExecuteProductionWidget import Ui_ExecuteProduction
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class ExecuteProductionWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExecuteProduction()
        self.ui.setupUi(self)

        self.ui.executeProductionButton.clicked.connect(self.executeProductionButtonClicked)
        
    def executeProductionButtonClicked(self):
        workOrderNumber = self.ui.executeWONumberComboBox.currentText()
        customer = self.ui.executeWOCustomerSelection.currentText()
        orderDate = self.ui.executeWODateInput.text()
        backCaseDetails = self.ui.executeWOBackCaseDetailsInput.currentText()
        drillingArrangement = self.ui.executeWODrillingArrangementSelection.currentText()
        quantity = self.ui.executeWOQuantityInput.text()
        productionDate = self.ui.executeWOProductionDateInput.text()
        shippingMethod = self.ui.executeWOShippingMethod.currentText()
        
        print("Following work order executed: ")
        print("Work Order Number: ", workOrderNumber)
        print("Customer: ", customer)
        print("Order Date: ", orderDate)
        print("Back Case Details: ", backCaseDetails)
        print("Drilling Arrangement: ", drillingArrangement)
        print("Quantity: ", quantity)
        print("Production Date: ", productionDate)
        print("Shipping Method: ", shippingMethod)
        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ExecuteProductionWidgetHandler()
    widget.show()
    app.exec()