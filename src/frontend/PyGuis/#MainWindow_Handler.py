#MainWindow_Handler

from MainWindow import Ui_MainWindow
from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QApplication, QMainWindow
# import classes from Work Order Manager, Production Systems Manager, Schedule Manager, Inventory Manager
from WorkOrderManagerHome_Handler import WorkOrderManagerHomeHandler
# Handler file not yet created for ProductionSystemsManagerWidget
# from ProductionSystemsManagerWidget_Handler import ProductionSystemsManagerWidgetHandler
from ProductionScheduleManagerWidget_Handler import ProductionScheduleManagerWidgetHandler
from InventoryManager_Handler import inventoryManagerHandler

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainMenuWorkOrderManagerButton.clicked.connect(self.mainMenuWorkOrderManagerButtonClicked)
        # self.ui.mainMenuProductionSystemsManagerButton.clicked.connect(self.mainMenuProductionSystemsManagerButtonClicked)
        self.ui.mainMenuScheduleManagerButton.clicked.connect(self.mainMenuScheduleManagerButtonClicked)
        self.ui.mainMenuInventoryManagerButton.clicked.connect(self.mainMenuInventoryManagerButtonClicked)

    def mainMenuWorkOrderManagerButtonClicked(self):
        self.workOrderManagerWidget = WorkOrderManagerHomeHandler()
        self.workOrderManagerWidget.show()

    # def mainMenuProductionSystemsManagerButtonClicked(self):
    #     self.productionSystemsManagerWidget = ProductionSystemsManagerWidgetHandler()
    #     self.productionSystemsManagerWidget.show()

    def mainMenuScheduleManagerButtonClicked(self):
        self.productionScheduleManagerWidget = ProductionScheduleManagerWidgetHandler()
        self.productionScheduleManagerWidget.show()

    def mainMenuInventoryManagerButtonClicked(self):
        self.inventoryManagerWidget = inventoryManagerHandler()
        self.inventoryManagerWidget.show()

    #     self.ui.mainMenuInventoryManagerButton.clicked.connect(self.showNewWindow)


    # def showNewWindow(self,checked):
    #     self.w = Ui_productionSchedulerWiget()
    #     self.w.show()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()