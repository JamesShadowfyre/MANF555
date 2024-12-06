#OperatorManagerWidget Handler

#Need to define what happens when users click buttons (will be opening the new widgets) - completed
#Need to replace the data that appears in the table with data from the database, in the INIT

from frontend.PyGuis.OperatorManagerWidget import Ui_operatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
# import secondary widget handlers
from frontend.PyGuis.AddNewOperatorWidget_Handler import AddNewOperatorHandler
from frontend.PyGuis.EditOperatorWidget_Handler import EditOperatorWidgetHandler
from frontend.PyGuis.DeleteOperatorWidget_Handler import DeleteOperatorWidgetHandler

from backend.apiAccessPoint import ApplicationHome

class OperatorManagerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_operatorWidget()
        self.ui.setupUi(self)
        self.updateTableData()

        self.ui.removeOperatorButton.clicked.connect(self.removeOperatorButtonClicked)
        self.ui.addNewOperatorButton.clicked.connect(self.addNewOperatorButtonClicked)
        self.ui.editOperatorButton.clicked.connect(self.editOperatorButtonClicked)



        #-----------------------------------------------------
        #Replace RHS of self.userData with the tie in
        #[User ID, Username, Rights [Bool]
        #----------------------------------------------------- 
        #self.userData = [["ID1", "user1",0], ["ID2", "user2",0], ["ID3", "user3",0]]
        api = ApplicationHome()
        self.userData = api.userFunctions('loadall')
        
        #Table Operations Begin -----
        # Clear the table before populating
        self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget.setRowCount(len(self.userData))
        self.ui.tableWidget.setColumnCount(3)  # Adjust columns if necessary
        self.ui.tableWidget.setHorizontalHeaderLabels(["Employee Number", "Username", "Admin Rights"]) 

        # Populate the table
        for row, data in enumerate(self.userData):
            for column, value in enumerate(data):
                # Convert rights (column 2) to human-readable text, e.g., Yes/No
                if column == 2:  # Assuming rights is the third column
                    item = qtw.QTableWidgetItem("Yes" if value else "No")
                else:
                    item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        #Table Operations End -----
        #  












    def removeOperatorButtonClicked(self):
        self.deleteOperatorWidget = DeleteOperatorWidgetHandler()
        self.deleteOperatorWidget.show()

    def addNewOperatorButtonClicked(self):
        self.addNewOperatorWidget = AddNewOperatorHandler()
        self.addNewOperatorWidget.show()

    def editOperatorButtonClicked(self):
        self.editOperatorWidget = EditOperatorWidgetHandler()
        self.editOperatorWidget.show()
        

    def updateTableData(self):
        #I want to read the data from the QLineEdit fields here
        pass

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = OperatorManagerWidgetHandler()
    widget.show()
    app.exec()