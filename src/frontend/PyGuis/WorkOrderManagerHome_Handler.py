#Work Order Manager Handler
#Need to construct a method to display the data from the tables that James is making
#Need to construct "View completed work orders" screen & connect

from WorkOrderManagerHome import Ui_WorkOrderManagerWidget
from CreateWorkOrderWidget_Handler import CreateNewWorkOrderHandler
from DeleteWorkOrderHandler import DeleteWorkOrderHandler
from EditWorkOrder_Handler import EditWorkOrderHandler
from CustomerManager_Handler import CustomerManagerHandler
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class WorkOrderManagerHomeHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

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
        if self.refreshClickCount != 0:
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("Refresh")
            msg_box.setText("Customer Data Refreshed")
            msg_box.exec()
        
        self.refreshClickCount += 1

        #need to write the code here that connects table columns to database

        


        
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = WorkOrderManagerHomeHandler()
    widget.show()
    app.exec()
