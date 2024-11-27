from KPI import Ui_Form

from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class KPIHandler(qtw.QWidget): 
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


#Code to launch widget
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = KPIHandler()
    widget.show()
    app.exec()