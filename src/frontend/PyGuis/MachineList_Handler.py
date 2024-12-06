from frontend.PyGuis.MachineList import Ui_MachineList
from backend.apiAccessPoint import ApplicationHome
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MachineListHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MachineList()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MachineListHandler()
    widget.show()
    app.exec()