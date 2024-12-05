from frontend.PyGuis.ExecuteProductionWidget import Ui_ExecuteProduction
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QDate

class ExecuteProductionWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExecuteProduction()
        self.ui.setupUi(self)

        self.ui.executeProductionButton.clicked.connect(self.executeProductionButtonClicked)
        
        #set all of these equal to database values
        workOrderList = ["","1","2","3","4"] #WO number - update with sql data
        customerList = ["cust1", "cust2", "cust3"] #update with sql data

        self.ui.executeWONumberComboBox.addItems(workOrderList)
        self.ui.executeWOCustomerSelection.addItems(customerList)
        self.ui.executeWODateInput.setDate(QDate(2000, 1, 1))
        self.ui.executeWOQuantityInput.setValue(0)
        self.ui.executeWOProductionDateInput.setDate(QDate(2000, 1, 1))
        self.ui.executeWODrillingArrangementSelection.clear()
        self.ui.executeWOBackCaseDetailsInput.setCurrentText("")
        self.ui.executeWOShippingMethod.setCurrentText("")

#Disable the entire UI except the "select WO combobox"
        # self.ui.executeWOCustomerSelection.setDisabled(True)
        self.ui.executeWODateInput.setDisabled(True)
        self.ui.executeWOBackCaseDetailsInput.setDisabled(True)
        self.ui.executeWODrillingArrangementSelection.setDisabled(True)
        self.ui.executeWOQuantityInput.setDisabled(True)
        self.ui.executeWOProductionDateInput.setDisabled(True)
        self.ui.executeWOShippingMethod.setEnabled(True)


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