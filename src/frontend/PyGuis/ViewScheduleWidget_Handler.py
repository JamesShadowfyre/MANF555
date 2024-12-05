from frontend.PyGuis.ViewScheduleWidget import Ui_Form
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class ViewScheudleWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.refreshButton.clicked.connect(self.refreshButtonClicked)

    def refreshButtonClicked(self):
        new_data = self.fetchWorkOrderData()
        tableWidget = self.ui.allWorkOrderTable

        for row_data in new_data:
            current_row_count = tableWidget.rowCount()
            tableWidget.insertRow(current_row_count)

            for col, value in enumerate(row_data):
                item = qtw.QTableWidgetItem(value)
                tableWidget.setItem(current_row_count, col, item)

    def fetchWorkOrderData(self):
        # Example placeholder for fetching work order data
        return [
            ["0001", "2024-12-06", "11:00 AM", "10 mins"],
            ["0002", "2024-12-08", "2:30 PM", "13 mins"],
        ]

     # Today Production Schedule table to list code
    def extractWorkOrderTableToList(self):
        WorkOrder_list = []
        tableWidget = self.ui.allWorkOrderTable
        rows = tableWidget.rowCount()
        columns = tableWidget.columnCount()


        for row in range(rows):
            row_data = []
            for col in range(columns):
                item = tableWidget.item(row, col)
                row_data.append(item.text() if item else "")  # Handle empty cells
            WorkOrder_list.append(row_data)

        return WorkOrder_list

    def printWorkOrderList(self):
        # Print data from tableWidget
        data_list = self.extractWorkOrderTableToList()
        print("Work Order table data as list:")
        for row in data_list:
            print(row)


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ViewScheudleWidgetHandler()
    widget.show()
    app.exec()