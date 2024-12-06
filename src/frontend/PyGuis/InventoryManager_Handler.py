from frontend.PyGuis.InventoryManager import Ui_InventoryManager
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

# import secondary widget handlers
from frontend.PyGuis.RecieveInventoryWidget_Handler import RecieveInventoryWidgetHandler
from frontend.PyGuis.PerformCycleCounts_Handler import updateInventoryHandler
from frontend.PyGuis.CreateNewInventory_Handler import CreateNewInventoryHandler
from frontend.PyGuis.LowInventoryAlarmSettingWidget_Handler import LowInventoryAlarmWidget

class inventoryManagerHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_InventoryManager ()
        self.ui.setupUi(self)

        #-----------------------------------------------------
        #There is no write data from the main screen, just read data. 
        #Replace RHS of self.invData_all and self.invdata_low with queries of the database 
        #Query for low should be for all inv with QTY <= Low Limit Inventory Alarm
        #["Internal Part ID", "Quantity", "Name", "Description", "Unit Cost ($)"] 
        #----------------------------------------------------- 

        self.invData_all = [["0111", 5, "Back Cover", "Black", 1],["0222", 6, "Back Cover", "Blue", "11"]]
        self.invData_low = [["0111", 5, "Back Cover", "Black", 1]]
        self.ui.addInventory.clicked.connect(self.addInventoryClicked)
        self.ui.performInvCycleCount.clicked.connect(self.performInvCycleCountClicked)
        self.ui.createNewInventoryItem.clicked.connect(self.createNewInventoryItemClicked)
        self.ui.lowInvAlarmSettings.clicked.connect(self.lowInvAlarmSettingsClicked)

        self.lowInvTableUpdate()
        self.allInvTableUpdate()

    def addInventoryClicked(self):
        self.recieveInventoryWidget = RecieveInventoryWidgetHandler()
        self.recieveInventoryWidget.show()

    def allInvTableUpdate(self):
        # Clear the table before populating
        self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget.setRowCount(len(self.invData_all))
        self.ui.tableWidget.setColumnCount(5)  # Adjust columns if necessary
        self.ui.tableWidget.setHorizontalHeaderLabels(["Internal Part ID", "Quantity", "Name", "Description", "Unit Cost ($)"]) 

        # Populate the table
        for row, data in enumerate(self.invData_all):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        #Table Operations End -----
        #  

    def lowInvTableUpdate(self):
        # Clear the table before populating
        self.ui.tableWidget_2.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget_2.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget_2.setRowCount(len(self.invData_low))
        self.ui.tableWidget_2.setColumnCount(5)  # Adjust columns if necessary
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Internal Part ID", "Quantity", "Name", "Description","Unit Cost ($)"]) 

        # Populate the table
        for row, data in enumerate(self.invData_low):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget_2.setItem(row, column, item)
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        #Table Operations End -----
        #  

    def performInvCycleCountClicked(self):
        self.performCycleCounts = updateInventoryHandler()
        self.performCycleCounts.show()

    def createNewInventoryItemClicked(self):
        self.createNewInventoryWidget = CreateNewInventoryHandler()
        self.createNewInventoryWidget.show()

    def lowInvAlarmSettingsClicked(self):
        self.LowInventoryAlarmSettingWidget = LowInventoryAlarmWidget()
        self.LowInventoryAlarmSettingWidget.show()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = inventoryManagerHandler()
    widget.show()
    app.exec()