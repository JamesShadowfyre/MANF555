from InventoryManager import Ui_InventoryManager
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

# import secondary widget handlers
from RecieveInventoryWidget_Handler import RecieveInventoryWidgetHandler
from PerformCycleCounts_Handler import updateInventoryHandler
from CreateNewInventory_Handler import CreateNewInventoryHandler
from LowInventoryAlarmSettingWidget_Handler import LowInventoryAlarmWidget

class inventoryManagerHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_InventoryManager ()
        self.ui.setupUi(self)

        self.ui.addInventory.clicked.connect(self.addInventoryClicked)
        self.ui.performInvCycleCount.clicked.connect(self.performInvCycleCountClicked)
        self.ui.createNewInventoryItem.clicked.connect(self.createNewInventoryItemClicked)
        self.ui.lowInvAlarmSettings.clicked.connect(self.lowInvAlarmSettingsClicked)

    def addInventoryClicked(self):
        self.recieveInventoryWidget = RecieveInventoryWidgetHandler()
        self.recieveInventoryWidget.show()

    def performInvCycleCountClicked(self):
        self.performCycleCounts = updateInventoryHandler()
        self.performCycleCounts.show()

    def createNewInventoryItemClicked(self):
        self.createNewInventoryWidget = CreateNewInventoryHandler()
        self.createNewInventoryWidget.show()

    def lowInvAlarmSettingsClicked(self):
        self.LowInventoryAlarmSettingWidget = LowInventoryAlarmWidget()
        self.LowInventoryAlarmSettingWidget.show()

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = inventoryManagerHandler()
    widget.show()
    app.exec()