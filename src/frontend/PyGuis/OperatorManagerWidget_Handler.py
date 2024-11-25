#OperatorManagerWidget Handler

#Need to define what happens when users click buttons (will be opening the new widgets)
#Need to replace the data that appears in the table with data from the database, in the INIT

from OperatorManagerWidget import Ui_operatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

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
        pass
    def addNewOperatorButtonClicked(self):
        pass
    def editOperatorButtonClicked(self):
        pass

    def updateTableData(self):
        #I want to read the data from the QLineEdit fields here
        pass

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = OperatorManagerWidgetHandler()
    widget.show()
    app.exec()



