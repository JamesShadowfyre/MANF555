#OperatorManagerWidget Handler

#Need to define what happens when users click buttons (will be opening the new widgets) - completed
#Need to replace the data that appears in the table with data from the database, in the INIT

from OperatorManagerWidget import Ui_operatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
# import secondary widget handlers
from AddNewOperatorWidget_Handler import AddNewOperatorHandler
from EditOperatorWidget_Handler import EditOperatorWidgetHandler
from DeleteOperatorWidget_Handler import DeleteOperatorWidgetHandler

class OperatorManagerWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_operatorWidget()
        self.ui.setupUi(self)
        self.updateTableData()

        self.ui.removeOperatorButton.clicked.connect(self.removeOperatorButtonClicked)
        self.ui.addNewOperatorButton.clicked.connect(self.addNewOperatorButtonClicked)
        self.ui.editOperatorButton.clicked.connect(self.editOperatorButtonClicked)

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

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = OperatorManagerWidgetHandler()
    widget.show()
    app.exec()