from frontend.PyGuis.DeleteOperatorWidget import Ui_DeleteOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class DeleteOperatorWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DeleteOperatorWidget()
        self.ui.setupUi(self)
        self.ui.deleteOperatorButton.clicked.connect(self.deleteOperatorButtonClicked)
    
    def deleteOperatorButtonClicked(self):
        operatorName =  self.ui.deleteOperatorComboBox.currentText()
        employeeNumber = self.ui.deleteEmployeeNumberBox.text()

        print("Deleted Operator Name: ",operatorName)
        print("Deleted Employee Number: ",employeeNumber)
        self.close()

# Code to launch widget
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = DeleteOperatorWidgetHandler()
    widget.show()
    app.exec()