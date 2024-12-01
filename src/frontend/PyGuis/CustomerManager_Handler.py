#Customer Manager Handler
#Code for "refresh Customer Data" needs to be completed

from CustomerManager import Ui_CustomerManagerWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class CustomerManagerHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_CustomerManagerWidget()
        self.ui.setupUi(self)

        self.refreshCustomerData()
                        
        self.ui.addNewCustomerButton.clicked.connect(self.addNewCustomerButtonClick)
        self.ui.pushButton_4.clicked.connect(self.editCustomerClick)
        self.ui.pushButton_3.clicked.connect(self.deleteCustomerClick)
        self.ui.pushButton_5.clicked.connect(self.refreshCustomerData)
        

    def addNewCustomerButtonClick(self):
        print("1")

    def editCustomerClick(self):
        print("2")

    def deleteCustomerClick(self):
        print("3")

    def refreshCustomerData(self): #this needs to be updated with the code to refresh table data
        print("4")

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CustomerManagerHandler()
    widget.show()
    app.exec()
