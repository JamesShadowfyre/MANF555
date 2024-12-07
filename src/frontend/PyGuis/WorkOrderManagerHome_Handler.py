#Work Order Manager Handler
#Need to construct a method to display the data from the tables that James is making
#Need to construct "View completed work orders" screen & connect

from frontend.PyGuis.WorkOrderManagerHome import Ui_WorkOrderManagerWidget
from frontend.PyGuis.CreateWorkOrderWidget_Handler import CreateNewWorkOrderHandler
from frontend.PyGuis.DeleteWorkOrderHandler import DeleteWorkOrderHandler
from frontend.PyGuis.EditWorkOrder_Handler import EditWorkOrderHandler
from frontend.PyGuis.CustomerManager_Handler import CustomerManagerHandler
from frontend.PyGuis.CompletedWorkOrdersWidget_Handler import CompletedWorkOrdersWidgetHandler
from backend.apiAccessPoint import ApplicationHome
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class WorkOrderManagerHomeHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.api = ApplicationHome()
        self.ui = Ui_WorkOrderManagerWidget()
        self.ui.setupUi(self)
        self.refreshClickCount = 0
        self.refreshWorkOrderData()
        
        self.ui.createWOButton.clicked.connect(self.createWorkOrderButtonClicked)
        self.ui.editWOButton.clicked.connect(self.editWorkOrderButtonClicked)
        self.ui.deleteWOButton.clicked.connect(self.deleteWorkOrderButtonClicked)
        self.ui.completedWOButton.clicked.connect(self.completedWorkOrdersButtonClicked)
        self.ui.customerManagerButton.clicked.connect(self.customerManagerButtonClicked)
        self.ui.RefreshData.clicked.connect(self.refreshWorkOrderData)
        self.ui.completedWOButton.clicked.connect(self.viewCompletedWOs)

    def viewCompletedWOs(self):
        self.ViewCompletedWO = CompletedWorkOrdersWidgetHandler()
        self.ViewCompletedWO.show()

    def createWorkOrderButtonClicked(self):
        self.CreateWO = CreateNewWorkOrderHandler()
        self.CreateWO.show()

    def editWorkOrderButtonClicked(self):
        self.EditWO = EditWorkOrderHandler()
        self.EditWO.show()

    def deleteWorkOrderButtonClicked(self):
        self.DeleteWO = DeleteWorkOrderHandler()
        self.DeleteWO.show()

    def completedWorkOrdersButtonClicked(self):
        pass

    def customerManagerButtonClicked(self):
        self.Customers = CustomerManagerHandler()
        self.Customers.show()

    def refreshWorkOrderData(self): #This updates the screen data
            #-----------------------------------------------------
            #James:
            # No writing of data occurs on this screen -  only the read information is needed
            # Replace RHS of self.userData with the tie in for data read. I've already built the function to convert the task code to a drilling description
            #["Work Order ID", "Scheduled Start Date", "Date Completed", "Account ID", "Drilling Arrangement", "Cost", "Operator"]
            #----------------------------------------------------- 
            #self.userData = [["WO1","15/12/2024","15/12/2024","ACCT-1",0, 10,"Operator1"], ["WO2","16/12/2024","16/12/2024","ACCT-2",1, 20,"Operator2"]]
            self.userData = self.api.setWorkOrderFunctions('loadOverview')
            #Table Operations Begin -----
            # Clear the table before populating
            self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
            self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

            # Set new row count and populate the table with new data
            self.ui.tableWidget.setRowCount(len(self.userData))
            self.ui.tableWidget.setColumnCount(7)  # Adjust columns if necessary
            self.ui.tableWidget.setHorizontalHeaderLabels(["Work Order ID", "Scheduled Start Date", "Date Completed", "Account ID", "Drilling Arrangement", "Cost", "Operator"]) 

            # Populate the table
            for row, data in enumerate(self.userData):
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

            if self.refreshClickCount != 0:
                msg_box = qtw.QMessageBox(self)
                msg_box.setWindowTitle("Refresh")
                msg_box.setText("Customer Data Refreshed")
                msg_box.exec()
        
            self.refreshClickCount += 1



        
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = WorkOrderManagerHomeHandler()
    widget.show()
    app.exec()
