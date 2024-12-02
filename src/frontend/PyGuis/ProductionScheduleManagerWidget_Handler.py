from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
# import secondary widget handlers
from CustomerManager_Handler import CustomerManagerHandler
from OperatorManagerWidget_Handler import OperatorManagerWidgetHandler
# from <> import <> (no modify schedule UI file)
# from <> import <> (no view schedule UI file)

class ProductionScheduleManagerWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_productionSchedulerWiget()
        self.ui.setupUi(self)

        self.ui.refreshButton.clicked.connect(self.refreshButtonClicked)
        self.ui.sManagerCustomerManagerButton.clicked.connect(self.customerManagerButtonClicked)
        self.ui.sManagerOperatorManagerButton.clicked.connect(self.operatorManagerButtonClicked)
        # modify schedule button clicked (UI not created yet)
        # self.ui.pushButton.clicked.connect(self.modifyScheduleButtonClicked)
        # # view schedule button clicked (UI not created yet)
        # self.ui.pushButton_2.clicked.connect(self.viewScheduleButtonClicked)
        # self.printTodaysDataList()
        # self.printOutstandingWorkOrderList()

    def refreshButtonClicked(self):
        self.printTodaysDataList()
        self.printOutstandingWorkOrderList()

    def customerManagerButtonClicked(self):
        self.customerManagerWidget = CustomerManagerHandler ()
        self.customerManagerWidget.show()

    def operatorManagerButtonClicked(self):
        self.addNewOperatorWidget = OperatorManagerWidgetHandler()
        self.addNewOperatorWidget.show()

    # def modifyScheduleButtonClicked(self):
    #     self.editOperatorWidget = <>()
    #     self.editOperatorWidget.show()

    # def viewScheduleButtonClicked(self):
    #     self.editOperatorWidget = <>()
    #     self.editOperatorWidget.show()

    # Today table code
    def extractTodaysDataToList(self):
        TodayData_list = []
        tableWidget = self.ui.tableWidget
        rows = tableWidget.rowCount()
        columns = tableWidget.columnCount()


        for row in range(rows):
            row_data = []
            for col in range(columns):
                item = tableWidget.item(row, col)
                row_data.append(item.text() if item else "")  # Handle empty cells
            TodayData_list.append(row_data)

        return TodayData_list

    def printTodaysDataList(self):
        # Print data from tableWidget
        data_list = self.extractTodaysDataToList()
        print("Today's Production Schedule table data as list:")
        for row in data_list:
            print(row)
    
# Outstanding Work Order list code
    def extractOutstandingWorkOrderToList(self):
        OutstandingWorkOrder_list = []
        tableWidget2 = self.ui.tableWidget_2
        rows = tableWidget2.rowCount()
        columns = tableWidget2.columnCount()


        for row in range(rows):
            row_data = []
            for col in range(columns):
                item = tableWidget2.item(row, col)
                row_data.append(item.text() if item else "")  # Handle empty cells
            OutstandingWorkOrder_list.append(row_data)

        return OutstandingWorkOrder_list

    def printOutstandingWorkOrderList(self):
        # Print data from tableWidget
        data_list = self.extractOutstandingWorkOrderToList()
        print("Oustanding Work Order table data as list:")
        for row in data_list:
            print(row)


        # # Extract data as a dictionary
        # data_dict = extractTodaysDataToList(tableWidget)
        # print("\nExtracted Data as Dictionary:")
        # for key, values in data_dict.items():
        #     print(f"{key}: {values}")

    # Call this function in your main application
    # printTodaysDataList(self.tableWidget)


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ProductionScheduleManagerWidgetHandler()
    widget.show()
    app.exec()