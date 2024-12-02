#Production Systems Manager Widget Handler

#MainWindow_Handler

from ProductionSystemsManagerWidget import Ui_productionSystemsManagerWidget
from ExecuteProductionWidget_Handler import ExecuteProductionWidgetHandler
from OperatorManagerWidget_Handler import OperatorManagerWidgetHandler
from KPI_Handler import KPIHandler 
from PyQt5 import QtWidgets as qtw

from PyQt5 import QtCore as qtc

class FactoryHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_productionSystemsManagerWidget()
        self.ui.setupUi(self)

        self.ui.executeProductionButton.clicked.connect(self.openExecute)
        self.ui.operatorManagerButton.clicked.connect(self.openOperators)
        self.ui.kPIButton.clicked.connect(self.openKPIs)

    def openExecute(self):
        self.exe = ExecuteProductionWidgetHandler()
        self.exe.show()
    
    def openOperators(self):
        self.ops = OperatorManagerWidgetHandler()
        self.ops.show()
    
    def openKPIs(self):
        self.kpis = KPIHandler()
        self.kpis.show()

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = FactoryHandler()
    widget.show()
    app.exec()



