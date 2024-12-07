
from frontend.PyGuis.CompletedWorkOrdersWidget import Ui_CompletedWorkOrders
#from backend.apiAccessPoint import ApplicationHome
#from CompletedWorkOrdersWidget import Ui_CompletedWorkOrders

from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class CompletedWorkOrdersWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_CompletedWorkOrders()
        self.ui.setupUi(self)

        self.getCompletedWOData()

    def getCompletedWOData(self): #This updates the screen data
        #-----------------------------------------------------
        #James:
        # No writing of data occurs on this screen -  only the read information is needed
        # Replace RHS of self.userData with the tie in for data read. I've already built the function to convert the task code to a drilling description
        # Ensure query filters by COMPLETED DATE isNOT BLANK
        #["Work Order ID", "Scheduled Start Date", "Date Completed", "Account ID", "Drilling Arrangement", "Cost", "Operator"]
        #----------------------------------------------------- 
        self.userData = [["WO1","15/12/2024","15/12/2024","ACCT-1",0, 10,"Operator1"], ["WO2","16/12/2024","16/12/2024","ACCT-2",1, 20,"Operator2"]]
        #self.userData = self.api.setWorkOrderFunctions('loadOverview')
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
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CompletedWorkOrdersWidgetHandler()
    widget.show()
    app.exec()