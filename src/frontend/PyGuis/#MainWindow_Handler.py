#MainWindow_Handler

from MainWindow import Ui_MainWindow
from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mainMenuInventoryManagerButton.clicked.connect(self.showNewWindow)


    def showNewWindow(self,checked):
        self.w = Ui_productionSchedulerWiget()
        self.w.show()

app = qtw.QApplication([])
widget = MainWindow()
widget.show()

app.exec()



