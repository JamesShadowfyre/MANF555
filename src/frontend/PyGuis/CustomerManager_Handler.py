#Customer Manager Handler
#Code for "refresh Customer Data" needs to be completed

from frontend.PyGuis.CustomerManager import Ui_CustomerManagerWidget
from frontend.PyGuis.RemoveCustomerWidget_Handler import RemoveCustomerWidgetHandler
from frontend.PyGuis.EditCustomerWidget_Handler import EditCustomerWidgetHandler
from frontend.PyGuis.AddCustomerWidget_Handler import AddCustomerWidgetHandler


from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class CustomerManagerHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()


        self.ui = Ui_CustomerManagerWidget()
        self.ui.setupUi(self)

        #-----------------------------------------------------
        #Replace RHS of self.userData with the tie in
        #[Account ID, Street Addr1, Street Addr2, City, Region, Postal Code, Canada, Email] - all strings
        #----------------------------------------------------- 

        self.userData = [["ACCT1","111 University Way","A","Kelowna","BC","V1V 1V1", "Canada", "university1@ubc.ca"], ["ACCT2","222 University Way","B","Kelowna","BC","V2V 2V2", "Canada", "university2@ubc.ca"]]
        
        
        self.refreshClickCount = 0
        self.refreshCustomerData()
        self.tableUpdate()
                        
        self.ui.addNewCustomerButton.clicked.connect(self.addNewCustomerButtonClick)
        self.ui.pushButton_4.clicked.connect(self.editCustomerClick)
        self.ui.pushButton_3.clicked.connect(self.deleteCustomerClick)
        self.ui.pushButton_5.clicked.connect(self.refreshCustomerData)

    def tableUpdate(self):
        # Clear the table before populating
        self.ui.customerDataWidget.clearContents()  # Clear all cell contents but keep the headers
        self.ui.customerDataWidget.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.customerDataWidget.setRowCount(len(self.userData))
        self.ui.customerDataWidget.setColumnCount(8)  # Adjust columns if necessary
        self.ui.customerDataWidget.setHorizontalHeaderLabels(["Account ID", "Street Addr. 1", "Street Addr. 2", "City", "Region", "Postal Code", "Country", "Email"]) 

        # Populate the table
        for row, data in enumerate(self.userData):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.customerDataWidget.setItem(row, column, item)
                #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        #Table Operations End -----
        #  
        
    def addNewCustomerButtonClick(self):
        self.addCust = AddCustomerWidgetHandler()
        self.addCust.show()


    def editCustomerClick(self):
        self.editCust = EditCustomerWidgetHandler()
        self.editCust.show()


    def deleteCustomerClick(self):
        self.DeleteCust = RemoveCustomerWidgetHandler()
        self.DeleteCust.show()


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
