from AddNewOperatorWidget import Ui_addNewOperatorWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class AddNewOperatorHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_addNewOperatorWidget()
        self.ui.setupUi(self)
        self.ui.saveOperatorButton.clicked.connect(self.saveOperatorButtonClicked)


    def saveOperatorButtonClicked(self):
        operatorName =  self.ui.newOperatorNameInput.text()
        employeeNumber = self.ui.newEmployeeNumberInput.text()
    
        print(operatorName)
        print(employeeNumber)
        pass


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AddNewOperatorHandler()
    widget.show()
    app.exec()