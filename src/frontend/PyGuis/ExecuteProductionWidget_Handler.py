from frontend.PyGuis.ExecuteProductionWidget import Ui_ExecuteProduction
from backend.apiAccessPoint import ApplicationHome
#from ExecuteProductionWidget import Ui_ExecuteProduction
from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QDate

class ExecuteProductionWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExecuteProduction()
        self.ui.setupUi(self)

        #-----------------------------------------------------
        # James:
        #Replace RHS of self.userData with the tie in
        #["Work Order ID", "Scheduled Start Date", "Date Completed", "Account ID", "Drilling Arrangement", "Cost", "Operator"]
        #-----------------------------------------------------
        self.api = ApplicationHome()
        # self.workOrdersData = [
        #     ["0098", "Steve", "2024-11-01", 50, "2024-12-07", "2L", "Black", "Customer Pickup"],
        #     ["0099", "Bob", "2024-11-29", 70, "2024-12-09", "2R", "Black", "Delivery (Other)"],
        #     ["0100", "Joe", "2024-12-01", 65, "2024-12-12", "ALL", "Black", "Delivery (Other)"]
        # ]
        self.workOrdersData = self.api.setWorkOrderFunctions('loadoverview')
        # Populate work order combo box
        workOrderIDs = [order[0] for order in self.workOrdersData]
        self.ui.executeWONumberComboBox.addItems(workOrderIDs)  # Add work order IDs to the combo box

        # Populate customer, drilling arrangement, and back case details combo boxes initially
        self.populateComboBoxes()
        self.tableUpdate()

        # Disable input fields initially
        self.disableFields()

        # Connect signals
        self.ui.executeProductionButton.clicked.connect(self.executeProductionButtonClicked)
        self.ui.executeWONumberComboBox.currentTextChanged.connect(self.updateUI)

        # Initial check to populate fields based on default selection
        self.updateUI(self.ui.executeWONumberComboBox.currentText())

    def tableUpdate(self):
            #Table Operations Begin -----
            # Clear the table before populating
            self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
            self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

            # Set new row count and populate the table with new data
            self.ui.tableWidget.setRowCount(len(self.workOrdersData))
            self.ui.tableWidget.setColumnCount(7)  # Adjust columns if necessary
            self.ui.tableWidget.setHorizontalHeaderLabels(["Work Order ID", "Scheduled Start Date", "Date Completed", "Account ID", "Drilling Arrangement", "Cost", "Operator"]) 

            # Populate the table
            for row, data in enumerate(self.workOrdersData):
                for column, value in enumerate(data):
                    # Convert task code (column 4) to drilling description
                    if column == 4:  # task code passed to is the fifth column
                        if value == 0:
                            item = qtw.QTableWidgetItem("No drilling")
                        if value == 1:
                            item = qtw.QTableWidgetItem("2x back holes")
                        if value == 2:
                            item = qtw.QTableWidgetItem("2x front holes")
                        if value == 3:
                            item = qtw.QTableWidgetItem("4x holes (2x front + 2x back)")
                    else:
                        item = qtw.QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(row, column, item)

            #Table Operations End -----

    def disableFields(self):
        # Disable all fields initially
        self.ui.executeWOCustomerSelection.setDisabled(True)
        self.ui.executeWODateInput.setDisabled(True)
        self.ui.executeWOBackCaseDetailsInput.setDisabled(True)
        self.ui.executeWODrillingArrangementSelection.setDisabled(True)
        self.ui.executeWOQuantityInput.setDisabled(True)
        self.ui.executeWOProductionDateInput.setDisabled(True)
        self.ui.executeWOShippingMethod.setDisabled(True)

    def populateComboBoxes(self):
        # Populate the combo boxes with the possible options

        # Populate customer selection with unique customers
        customers = list(set(order[1] for order in self.workOrdersData))
        self.ui.executeWOCustomerSelection.addItems(customers)
        
        # Populate drilling arrangement with unique arrangements
        drillingArrangements = list(set(order[5] for order in self.workOrdersData))
        self.ui.executeWODrillingArrangementSelection.addItems(drillingArrangements)
        
        # Populate back case details with unique details
        backCaseDetails = list(set(order[6] for order in self.workOrdersData))
        self.ui.executeWOBackCaseDetailsInput.addItems(backCaseDetails)

    def updateUI(self, workOrderNumber):
        print(f"Updating UI for work order number: {workOrderNumber}")  # Debugging line

        # Find the matching work order using `next()`
        matchingOrder = next((order for order in self.workOrdersData if order[0] == workOrderNumber), None)

        if matchingOrder:
            # Debugging line to show found order
            print(f"Found matching order: {matchingOrder}")
            
            # Populate customer selection QComboBox
            self.ui.executeWOCustomerSelection.setCurrentText(matchingOrder[1])  # Customer
            print(f"Customer: {matchingOrder[1]} set in executeWOCustomerSelection")  # Debugging line

            # Populate order date QDateEdit
            self.ui.executeWODateInput.setDate(QDate.fromString(matchingOrder[2], "yyyy-MM-dd"))  # Order Date
            print(f"Order Date: {matchingOrder[2]} set in executeWODateInput")  # Debugging line

            # Populate quantity QSpinBox
            self.ui.executeWOQuantityInput.setValue(matchingOrder[3])  # Quantity
            print(f"Quantity: {matchingOrder[3]} set in executeWOQuantityInput")  # Debugging line

            # Populate production date QDateEdit
            self.ui.executeWOProductionDateInput.setDate(QDate.fromString(matchingOrder[4], "yyyy-MM-dd"))  # Production Date
            print(f"Production Date: {matchingOrder[4]} set in executeWOProductionDateInput")  # Debugging line

            # Populate drilling arrangement QComboBox
            self.ui.executeWODrillingArrangementSelection.setCurrentText(matchingOrder[5])  # Drilling Arrangement
            print(f"Drilling Arrangement: {matchingOrder[5]} set in executeWODrillingArrangementSelection")  # Debugging line

            # Populate back case details QComboBox
            self.ui.executeWOBackCaseDetailsInput.setCurrentText(matchingOrder[6])  # Back Case Details
            print(f"Back Case Details: {matchingOrder[6]} set in executeWOBackCaseDetailsInput")  # Debugging line

            # Populate shipping method QComboBox
            self.ui.executeWOShippingMethod.setCurrentText(matchingOrder[7])  # Shipping Method
            print(f"Shipping Method: {matchingOrder[7]} set in executeWOShippingMethod")  # Debugging line

        else:
            # Disable fields if no matching order is found
            self.disableFields()

    def executeProductionButtonClicked(self):
        # Collect data from the UI
        workOrderNumber = self.ui.executeWONumberComboBox.currentText()
        customer = self.ui.executeWOCustomerSelection.currentText()
        orderDate = self.ui.executeWODateInput.text()
        backCaseDetails = self.ui.executeWOBackCaseDetailsInput.currentText()
        drillingArrangement = self.ui.executeWODrillingArrangementSelection.currentText()
        quantity = self.ui.executeWOQuantityInput.text()
        productionDate = self.ui.executeWOProductionDateInput.text()
        shippingMethod = self.ui.executeWOShippingMethod.currentText()

        # Print the collected data (replace with actual database save)
        print("Following work order executed: ")
        print(f"Work Order Number: {workOrderNumber}")
        print(f"Customer: {customer}")
        print(f"Order Date: {orderDate}")
        print(f"Back Case Details: {backCaseDetails}")
        print(f"Drilling Arrangement: {drillingArrangement}")
        print(f"Quantity: {quantity}")
        print(f"Production Date: {productionDate}")
        print(f"Shipping Method: {shippingMethod}")

        # Close the widget after execution
        self.close()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ExecuteProductionWidgetHandler()
    widget.show()
    app.exec()
