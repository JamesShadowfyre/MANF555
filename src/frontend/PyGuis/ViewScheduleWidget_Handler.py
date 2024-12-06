from frontend.PyGuis.ViewScheduleWidget import Ui_Form
#from ViewScheduleWidget import Ui_Form
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class ViewScheudleWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #Update the RHS of these entities to correspond to the table entries
        #-----------------------------------------------------
        #read customer data from table
        #["Work Order ID", "Scheduled Start Date", "Scheduled Start Time", "Estimated Runtime (minutes)", "Production Qty", "Cost ($)", "Operator"]
        #-----------------------------------------------------

        self.userData = [["WO1","15/12/2024","08:00",10, 1,4, "Operator1"], ["WO2","15/12/2024","09:00",15, 2,5, "Operator2"], ["WO3","15/12/2024","10:00",20, 3,6, "Operator3"]]

        self.ui.refreshButton.clicked.connect(self.table1Update)
        self.table1Update()

    def table1Update(self):
        # Clear the table before populating
        self.ui.allWorkOrderTable.clearContents()  # Clear all cell contents but keep the headers
        self.ui.allWorkOrderTable.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.allWorkOrderTable.setRowCount(len(self.userData))
        self.ui.allWorkOrderTable.setColumnCount(7)  # Adjust columns if necessary
        self.ui.allWorkOrderTable.setHorizontalHeaderLabels(["Work Order ID", "Scheduled Start Date", "Scheduled Start Time", "Estimated Runtime (minutes)", "Production Qty", "Cost ($)", "Operator"]) 

        # Populate the table
        for row, data in enumerate(self.userData):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.allWorkOrderTable.setItem(row, column, item)
        #End table ops


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ViewScheudleWidgetHandler()
    widget.show()
    app.exec()