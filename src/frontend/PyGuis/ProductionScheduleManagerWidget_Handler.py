from frontend.PyGuis.ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
# import secondary widget handlers
from frontend.PyGuis.CustomerManager_Handler import CustomerManagerHandler
from frontend.PyGuis.OperatorManagerWidget_Handler import OperatorManagerWidgetHandler
from frontend.PyGuis.ViewScheduleWidget_Handler import ViewScheudleWidgetHandler 
# from <> import <> (no view schedule UI file)

class ProductionScheduleManagerWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_productionSchedulerWiget()
        self.ui.setupUi(self)

        #Update the RHS of these entities to correspond to the table entries
        #-----------------------------------------------------
        #James
        # read customer data from table
        #["Work Order ID", "Scheduled Start Date", "Scheduled Start Time", "Estimated Runtime (minutes)", "Production Qty", "Cost ($)", "Operator"]
        #userData is the today's list (scheduled startdate is TODAY in sql)
        #userData_2 is the outstanding WO (compltion_date is EMPTY in sql)

        #No Write data from this screen
        #-----------------------------------------------------



        self.userData = [["WO1","15/12/2024","08:00",10, 1,4, "Operator1"], ["WO2","15/12/2024","09:00",15, 2,5, "Operator2"], ["WO3","15/12/2024","10:00",20, 3,6, "Operator3"]]
        self.userData_2 = [["WO4","15/12/2024","08:00",10, 1,4, "Operator4"], ["WO5","15/12/2024","09:00",15, 2,5, "Operator5"], ["WO6","15/12/2024","10:00",20, 3,6, "Operator6"]]
        self.ui.refreshButton.clicked.connect(self.refreshButtonClicked)
        self.ui.sManagerCustomerManagerButton.clicked.connect(self.customerManagerButtonClicked)
        self.ui.sManagerOperatorManagerButton.clicked.connect(self.operatorManagerButtonClicked)

        self.ui.pushButton_2.clicked.connect(self.viewScheduleButtonClicked)

        # modify schedule button clicked (UI not created yet)
        # self.ui.pushButton.clicked.connect(self.modifyScheduleButtonClicked)
        # view schedule button clicked (UI not created yet)
        # self.printTodaysDataList()
        # self.printOutstandingWorkOrderList()

        self.extractOutstandingWorkOrderToList()
        self.extractTodaysDataToList()

    def refreshButtonClicked(self):
        self.extractTodaysDataToList()
        self.extractOutstandingWorkOrderToList()
        #self.printTodaysDataList()
        #self.printOutstandingWorkOrderList()


    def extractTodaysDataToList(self): #tablewidget
        # Clear the table before populating
        self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget.setRowCount(len(self.userData))
        self.ui.tableWidget.setColumnCount(7)  # Adjust columns if necessary
        self.ui.tableWidget.setHorizontalHeaderLabels(["Work Order ID", "Scheduled Start Date", "Scheduled Start Time", "Estimated Runtime (minutes)", "Production Qty", "Cost ($)", "Operator"]) 

        # Populate the table
        for row, data in enumerate(self.userData):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)

        #End table ops

    # def printTodaysDataList(self): #tablewidget_2
    #     # Print data from tableWidget
    #     data_list = self.extractTodaysDataToList()
    #     print("Today's Production Schedule table data as list:")
    #     for row in data_list:
    #         print(row)
    

    def extractOutstandingWorkOrderToList(self):
        # Clear the table before populating
        self.ui.tableWidget_2.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget_2.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget_2.setRowCount(len(self.userData_2))
        self.ui.tableWidget_2.setColumnCount(7)  # Adjust columns if necessary
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Work Order ID", "Scheduled Start Date", "Scheduled Start Time", "Estimated Runtime (minutes)", "Production Qty", "Cost ($)", "Operator"]) 

        # Populate the table
        for row, data in enumerate(self.userData_2):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget_2.setItem(row, column, item)
        #End table ops

    # def printOutstandingWorkOrderList(self):
    #     # Print data from tableWidget
    #     data_list = self.extractOutstandingWorkOrderToList()
    #     print("Oustanding Work Order table data as list:")
    #     for row in data_list:
    #         print(row)


        # # Extract data as a dictionary
        # data_dict = extractTodaysDataToList(tableWidget)
        # print("\nExtracted Data as Dictionary:")
        # for key, values in data_dict.items():
        #     print(f"{key}: {values}")

    # Call this function in your main application
    # printTodaysDataList(self.tableWidget)

    #Navigation

    def customerManagerButtonClicked(self):
        self.customerManagerWidget = CustomerManagerHandler ()
        self.customerManagerWidget.show()

    def operatorManagerButtonClicked(self):
        self.addNewOperatorWidget = OperatorManagerWidgetHandler()
        self.addNewOperatorWidget.show()

    # def modifyScheduleButtonClicked(self):
    #     self.editOperatorWidget = <>()
    #     self.editOperatorWidget.show()

    def viewScheduleButtonClicked(self):
        self.viewScheduleWidget = ViewScheudleWidgetHandler()
        self.viewScheduleWidget.show()
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ProductionScheduleManagerWidgetHandler()
    widget.show()
    app.exec()