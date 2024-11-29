from ExecuteProductionWidget import Ui_ExecuteProduction
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class ExecuteProductionWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExecuteProduction()
        self.ui.setupUi(self)

        

# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ExecuteProductionWidgetHandler()
    widget.show()
    app.exec()