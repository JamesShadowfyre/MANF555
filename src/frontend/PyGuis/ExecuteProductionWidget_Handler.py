from frontend.PyGuis.ExecuteProductionWidget import Ui_ExecuteProduction
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QDate

class ExecuteProductionWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExecuteProduction()
        self.ui.setupUi(self)

        self.ui.executeProductionButton.clicked.connect(self.executeProductionButtonClicked)
        
        # Mock data to simulate fetching from a database
        self.workOrdersData = {
            "0098": {
                "customer": "Steve",
                "orderDate": "2024-11-01",
                "quantity": 50,
                "productionDate": "2024-12-07",
                "drillingArrangement": "2L",
                "backCaseDetails": "Black",
                "shippingMethod": "Customer Pickup"
            },
            "0099": {
                "customer": "Bob",
                "orderDate": "2024-11-29",
                "quantity": 70,
                "productionDate": "2024-12-09",
                "drillingArrangement": "ALL",
                "backCaseDetails": "Black",
                "shippingMethod": "Delivery (Other)"
            },
            "0100": {
                "customer": "Joe",
                "orderDate": "2024-12-01",
                "quantity": 65,
                "productionDate": "2024-12-12",
                "drillingArrangement": "ALL",
                "backCaseDetails": "Black",
                "shippingMethod": "Delivery (Other)"
            }
            
        }

        # Add work orders to the combo box
        workOrderList = ["","0098", "0099", "0100"]  # Mock work order numbers
        self.ui.executeWONumberComboBox.addItems(workOrderList)

        # Mock list for customers, drilling arrangements, and back case details
        self.customers = ["Steve", "Bob", "Joe"]  # customer data
        self.backCaseDetailsList = ["Black", "Blue", "Red"]  # Back case details data
        self.drillingArrangements = ["2L", "2R", "ALL", "0"]  # Drilling arrangements data

        # Populate the combo boxes for customer, back case details, and drilling arrangements
        self.ui.executeWOCustomerSelection.addItems(self.customers)
        self.ui.executeWOBackCaseDetailsInput.addItems(self.backCaseDetailsList)
        self.ui.executeWODrillingArrangementSelection.addItems(self.drillingArrangements)

        # Initialize fields (optional)
        self.ui.executeWODateInput.setDate(QDate(2000, 1, 1))
        self.ui.executeWOQuantityInput.setValue(0)
        self.ui.executeWOProductionDateInput.setDate(QDate(2000, 1, 1))
        self.ui.executeWOShippingMethod.setCurrentText("")

        # Disable fields initially
        self.disableFields()

        # Connect the combo box text change to autofill function
        self.ui.executeWONumberComboBox.currentTextChanged.connect(self.autofillFields)

    def disableFields(self):
        self.ui.executeWODateInput.setDisabled(True)
        self.ui.executeWOBackCaseDetailsInput.setDisabled(True)
        self.ui.executeWODrillingArrangementSelection.setDisabled(True)
        self.ui.executeWOQuantityInput.setDisabled(True)
        self.ui.executeWOProductionDateInput.setDisabled(True)
        self.ui.executeWOShippingMethod.setDisabled(True)

    def autofillFields(self):
        # Get the selected work order number
        workOrderNumber = self.ui.executeWONumberComboBox.currentText()

        # If a valid work order is selected and it's not empty
        if workOrderNumber and workOrderNumber in self.workOrdersData:
            # Get the corresponding data for the work order
            data = self.workOrdersData[workOrderNumber]

            # Populate the fields with the data
            self.ui.executeWOCustomerSelection.setCurrentText(data["customer"])
            self.ui.executeWODateInput.setDate(QDate.fromString(data["orderDate"], "yyyy-MM-dd"))
            self.ui.executeWOQuantityInput.setValue(data["quantity"])
            self.ui.executeWOProductionDateInput.setDate(QDate.fromString(data["productionDate"], "yyyy-MM-dd"))
            self.ui.executeWODrillingArrangementSelection.setCurrentText(data["drillingArrangement"])  # Autofill Drilling Arrangement
            self.ui.executeWOBackCaseDetailsInput.setCurrentText(data["backCaseDetails"])
            self.ui.executeWOShippingMethod.setCurrentText(data["shippingMethod"])

            # Enable the fields after autofilling
            self.enableFields()
        else:
            # Clear and disable fields if no valid selection is made
            self.clearFields()
            self.disableFields()

    def enableFields(self):
        self.ui.executeWODateInput.setEnabled(True)
        self.ui.executeWOBackCaseDetailsInput.setEnabled(True)
        self.ui.executeWODrillingArrangementSelection.setEnabled(True)
        self.ui.executeWOQuantityInput.setEnabled(True)
        self.ui.executeWOProductionDateInput.setEnabled(True)
        self.ui.executeWOShippingMethod.setEnabled(True)

    def clearFields(self):
        self.ui.executeWOCustomerSelection.setCurrentText("")
        self.ui.executeWODateInput.setDate(QDate(2000, 1, 1))
        self.ui.executeWOQuantityInput.setValue(0)
        self.ui.executeWOProductionDateInput.setDate(QDate(2000, 1, 1))
        self.ui.executeWODrillingArrangementSelection.clear()
        self.ui.executeWOBackCaseDetailsInput.setCurrentText("")
        self.ui.executeWOShippingMethod.setCurrentText("")

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
