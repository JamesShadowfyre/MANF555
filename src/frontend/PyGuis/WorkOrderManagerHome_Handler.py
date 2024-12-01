#Work Order Manager Handler
#Need to construct a method to display the data from the tables that James is making

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

        self.showWorkOrderData()
        
        self.ui.createWOButton.clicked.connect(self.createWorkOrderButtonClicked)
        self.ui.editWOButton.clicked.connect(self.editWorkOrderButtonClicked)
        self.ui.deleteWOButton.clicked.connect(self.deleteWorkOrderButtonClicked)
        self.ui.completedWOButton.clicked.connect(self.completedWorkOrdersButtonClicked)
        self.ui.customerManagerButton.clicked.connect(self.customerManagerButtonClicked)

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
        pass


        
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = WorkOrderManagerHomeHandler()
    widget.show()
    app.exec()
