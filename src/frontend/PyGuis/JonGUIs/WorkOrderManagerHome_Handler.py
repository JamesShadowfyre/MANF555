#Work Order Manager Handler

#New User Widget handler

from WorkOrderManagerHome import Ui_WorkOrderManagerWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class WorkOrderManagerHomeHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_WorkOrderManagerWidget()
        self.ui.setupUi(self)

    def createWorkOrderButtonClicked(self):
        pass 

    def editWorkOrderButtonClicked(self):
        pass

    def deleteWorkOrderButtonClicked(self):
        pass

    def completedWorkOrdersButtonClicked(self):
        pass

    def customerManagerButtonClicked(self):
        pass

        
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = WorkOrderManagerHomeHandler()
    widget.show()
    app.exec()
