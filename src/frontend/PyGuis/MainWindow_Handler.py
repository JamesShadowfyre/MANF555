#MainWindow_Handler
from MainWindow import Ui_MainWindow
from WorkOrderManagerHome_Handler import WorkOrderManagerHomeHandler
# from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mainMenuWorkOrderManagerButton.clicked.connect(self.openWorkOrderTab)

    def openWorkOrderTab(self):
        self.openWOTab = WorkOrderManagerHomeHandler()
        self.openWOTab.show()

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



