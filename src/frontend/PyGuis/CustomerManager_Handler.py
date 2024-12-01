#Customer Manager Handler
#Code for "refresh Customer Data" needs to be completed

from CustomerManager import Ui_CustomerManagerWidget
from RemoveCustomerWidget_Handler import RemoveCustomerWidgetHandler
from EditCustomerWidget_Handler import EditCustomerWidgetHandler
from AddCustomerWidget_Handler import AddCustomerWidgetHandler
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class CustomerManagerHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_CustomerManagerWidget()
        self.ui.setupUi(self)

        self.refreshClickCount = 0
        self.refreshCustomerData()
                        
        self.ui.addNewCustomerButton.clicked.connect(self.addNewCustomerButtonClick)
        self.ui.pushButton_4.clicked.connect(self.editCustomerClick)
        self.ui.pushButton_3.clicked.connect(self.deleteCustomerClick)
        self.ui.pushButton_5.clicked.connect(self.refreshCustomerData)

        
    def addNewCustomerButtonClick(self):
        self.addCust = AddCustomerWidgetHandler()
        self.addCust.show()
        print("1")

    def editCustomerClick(self):
        self.editCust = EditCustomerWidgetHandler()
        self.editCust.show()
        print("2")

    def deleteCustomerClick(self):
        self.DeleteCust = RemoveCustomerWidgetHandler()
        self.DeleteCust.show()
        print("3")

    def refreshCustomerData(self): #this needs to be updated with the code to refresh table data
        if self.refreshClickCount != 0:   
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("Refresh")
            msg_box.setText("Customer Data Refreshed")
            msg_box.exec()
        
        self.refreshClickCount += 1


if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = CustomerManagerHandler()
    widget.show()
    app.exec()
