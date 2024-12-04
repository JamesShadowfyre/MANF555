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
        pass


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

    def printTodaysDataList(self):
        # Print data from tableWidget
        data_list = self.extractWorkOrderTableToList()
        print("Today's Production Schedule table data as list:")
        for row in data_list:
            print(row)


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ViewScheudleWidgetHandler()
    widget.show()
    app.exec()