#Production Systems Manager Widget Handler

#MainWindow_Handler

from frontend.PyGuis.ProductionSystemsManagerWidget import Ui_productionSystemsManagerWidget
from frontend.PyGuis.ExecuteProductionWidget_Handler import ExecuteProductionWidgetHandler
from frontend.PyGuis.OperatorManagerWidget_Handler import OperatorManagerWidgetHandler
from frontend.PyGuis.KPI_Handler import KPIHandler 
from frontend.PyGuis.MachineList_Handler import MachineListHandler 
from PyQt5 import QtWidgets as qtw

from PyQt5 import QtCore as qtc

class FactoryHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_productionSystemsManagerWidget()
        self.ui.setupUi(self)

        self.ui.executeProductionButton.clicked.connect(self.openExecute)
        self.ui.operatorManagerButton.clicked.connect(self.openOperators)
        self.ui.kpiButton.clicked.connect(self.openKPIs)
        self.ui.machineListButton.clicked.connect(self.openMachineList)

    def openExecute(self):
        self.exe = ExecuteProductionWidgetHandler()
        self.exe.show()
    
    def openOperators(self):
        self.ops = OperatorManagerWidgetHandler()
        self.ops.show()
    
    def openKPIs(self):
        self.kpis = KPIHandler()
        self.kpis.show()

    def openMachineList(self):
        self.kpis = MachineListHandler()
        self.kpis.show()

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = FactoryHandler()
    widget.show()
    app.exec()



