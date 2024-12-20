#MainWindow_Handler
from frontend.PyGuis.MainWindow import Ui_MainWindow
from frontend.PyGuis.WorkOrderManagerHome_Handler import WorkOrderManagerHomeHandler
from frontend.PyGuis.ProductionSystemsManagerWidget_Handler import FactoryHandler
from frontend.PyGuis.ProductionScheduleManagerWidget_Handler import ProductionScheduleManagerWidgetHandler
from frontend.PyGuis.InventoryManager_Handler import inventoryManagerHandler
from frontend.PyGuis.AboutWidget_Handler import AboutWidgetHandler
from frontend.PyGuis.UserManagerWidget_Handler import UserManagerWidgetHandler
from backend.apiAccessPoint import ApplicationHome
from PyQt5 import QtWidgets as qtw
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.api = ApplicationHome()
        self.ui.setupUi(self)
        self.keepRefreshing = True

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.MainWindowGUIRefresh)
        self.timer.start(1000) 

        #-----------------------------------------------------
        #There is no write data from the main screen, just read data. 
        #Replace RHS of self.userData with the tie in
        #[Work Order ID, Scheduled Start Date, Scheduled Start Time, Estimated Runtime (minutes), Production Qty, Cost ($)]; format is str, date, date/time, duration, int, string
        #----------------------------------------------------- 
        self.userData = self.api.setWorkOrderFunctions('loadmain') #[["WO1","15/12/2024","08:00",10, 1,4], ["WO2","15/12/2024","09:00",15, 2,5], ["WO1","15/12/2024","10:00",20, 3,6]]

        #widget data
        self.KPIMethod()
        self.prod_data()
        self.LoggedInUserData()
        self.MainWindowGUIRefresh()
        self.tableUpdate()

        self.ui.mainMenuWorkOrderManagerButton.clicked.connect(self.openWorkOrderTab)
        self.ui.mainMenuScheduleManagerButton.clicked.connect(self.openProductionSchedulerTab)
        self.ui.mainMenuProductionSystemsManagerButton.clicked.connect(self.openFactoryManagerTab)
        self.ui.mainMenuInventoryManagerButton.clicked.connect(self.openInventoryManagerTab)

        #setting elements to be READ ONLY be the user
        self.ui.lineEdit.setReadOnly(True)
        self.ui.lineEdit_2.setReadOnly(True)
        self.ui.lineEdit_3.setReadOnly(True)
        self.ui.lineEdit_4.setReadOnly(True)
        self.ui.lineEdit_5.setReadOnly(True)
        self.ui.lineEdit_6.setReadOnly(True)
        self.ui.lineEdit_7.setReadOnly(True)
        self.ui.lineEdit_8.setReadOnly(True)
        
        #menu navigation clicks
        self.ui.actionAdd_Inventory.triggered.connect(self.disabledMenu)
        self.ui.actionAdd_New_Customer.triggered.connect(self.disabledMenu)
        self.ui.actionAdd_New_Operator.triggered.connect(self.disabledMenu)
        self.ui.actionCustomers.triggered.connect(self.disabledMenu)
        self.ui.actionAdd_Inventory.triggered.connect(self.disabledMenu)
        self.ui.actionMetrics.triggered.connect(self.disabledMenu)
        self.ui.actionNew_Work_Order.triggered.connect(self.disabledMenu)
        self.ui.actionFull_Window.triggered.connect(self.disabledMenu)
        self.ui.actionMinimize.triggered.connect(self.disabledMenu)
        self.ui.actionView_Operators.triggered.connect(self.disabledMenu)
        self.ui.actionView_Work_Orders.triggered.connect(self.disabledMenu)
        self.ui.actionView_Inventory.triggered.connect(self.disabledMenu)
        self.ui.actionTutorials.triggered.connect(self.disabledMenu)
        self.ui.actionSign_Out.triggered.connect(self.disabledMenu)

        #these ones are connected and operational
        self.ui.actionAbout.triggered.connect(self.openAbout)
        self.ui.actionFacility_Overview.triggered.connect(self.openFactoryManagerTab)
        self.ui.actionScheduler.triggered.connect(self.openProductionSchedulerTab)
        self.ui.menuInventory_Manager.triggered.connect(self.openInventoryManagerTab)
        self.ui.menuProduction_Systems_Manager.triggered.connect(self.openFactoryManagerTab)
        self.ui.menuSchedule_Manager.triggered.connect(self.openProductionSchedulerTab)
        self.ui.menuWork_Order_Manager.triggered.connect(self.openWorkOrderTab)
        self.ui.menuUser_Manager.triggered.connect(self.openUserManager)
        self.ui.actionExit.triggered.connect(self.ExitFunction)

    ### Updating the visual elements on the screen with data
    # 
    # 
    # 

    def tableUpdate(self):
         # Clear the table before populating
        self.ui.tableWidget.clearContents()  # Clear all cell contents but keep the headers
        self.ui.tableWidget.setRowCount(0)  # Reset row count to zero

        # Set new row count and populate the table with new data
        self.ui.tableWidget.setRowCount(len(self.userData))
        self.ui.tableWidget.setColumnCount(6)  # Adjust columns if necessary
        self.ui.tableWidget.setHorizontalHeaderLabels(["Work Order ID", "Scheduled Start Date", "Scheduled Start Time", "Estimated Runtime (minutes)", "Production Qty", "Cost ($)"]) 

        # Populate the table
        for row, data in enumerate(self.userData):
            for column, value in enumerate(data):
                item = qtw.QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row, column, item)
                #self.ui.tableWidget.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        #Table Operations End -----
        #  

    def LoggedInUserData(self):
        self.ui.userIdTextBrowser.setText(self.api.userFunctions('get'))

    def KPIMethod(self):
        OEE = self.api.calculateMetrics('OEE')*100
        FPFY = self.api.calculateMetrics('FPFY')*100
        TSP = self.api.calculateMetrics('TSP')

        #I'm sure that some functions are going to be needed to calculate the OEE. Let me know how I can help, James.

        #update GUI elements
        self.ui.OEEValue.display(OEE)
        self.ui.FPFYValue.display(FPFY)
        self.ui.TSP_Value.display(TSP)

    def prod_data(self):

        #-----------------------------------------------------
        #James:  
        #
        #Queries will need to be generated from the database for the objects below:
        #----------------------------------------------------- 

        lastWOComplete = "4" #replace with sql query for WOs - to make life easy we can -'ve index  the previous WO in the table
        WOInProgress = "5" #not sure how you'll pull this one
        NextWO = "6" #replace with sql query for WOs - to make life easy we can index the next WO in the table
        operator = "operator_str"
        WOsCompletedToday =  "7" #replace with sql query for WOs with "completed date" field = TODAY()
        WOScheduledForToday = "8" #replace with sql query for WOs with "scheduled date" field = TODAY()
        UnitsProducedToday =  "9" #replace with sql query for sum(Quantity) with "completed date" field = TODAY()
        AvgWOFullfillmentTime = "01:20" #replace with sql query for sum(WOEndTime - WOStartime)/count(WO) with "completed date" field = TODAY()
        lowInvAlarmStatus = 1 #assuming this is managed as a binary alarm code; 0 is alarm OFF; 1 is alarm 1
        prodstatus = 1 #assuming this is managed as a binary alarm code; 0 is no production; 1 is production occuring


        WOCompletionPercentage = (int(WOsCompletedToday) / int(WOScheduledForToday))*100

        #conditional screens 
        if lowInvAlarmStatus == 1:
            self.ui.label_20.setText("Low Inventory Detected")
            self.ui.label_20.setStyleSheet("background-color: red; color: black;")
        else:
            self.ui.label_20.setText("Inventory OK")
            self.ui.label_20.setStyleSheet("background-color: white; color: black;")

        if prodstatus == 1:
            self.ui.station1Status_3.setText("Producing")
            self.ui.station1Status_3.setStyleSheet("background-color: green; color: white;")
        else:
            self.ui.station1Status_3.setText("Available for Production")
            self.ui.station1Status_3.setStyleSheet("background-color: white; color: black;")

        self.ui.progressBar.setValue(int(WOCompletionPercentage))

        #Updating other GUI elements
        self.ui.lineEdit_6.setText(lastWOComplete)
        self.ui.lineEdit_7.setText(NextWO)
        self.ui.lineEdit_8.setText(WOInProgress)
        self.ui.lineEdit_5.setText(operator)
        self.ui.lineEdit.setText(WOsCompletedToday)
        self.ui.lineEdit_2.setText(WOScheduledForToday)
        self.ui.lineEdit_3.setText(UnitsProducedToday)
        self.ui.lineEdit_4.setText(AvgWOFullfillmentTime)
        

    ###Screen navigations 
    def ExitFunction(self):
        self.close()
            
    def openAbout(self):
        self.about = AboutWidgetHandler()
        self.about.show()

    def openWorkOrderTab(self):
         self.openWOTab = WorkOrderManagerHomeHandler()
         self.openWOTab.show()

    def openFactoryManagerTab(self):
        self.openFactory = FactoryHandler()
        self.openFactory.show()

    def openInventoryManagerTab(self):
        self.invmanage = inventoryManagerHandler()
        self.invmanage.show()
    
    def openProductionSchedulerTab(self):
        self.prodsched = ProductionScheduleManagerWidgetHandler()
        self.prodsched.show()

    def openUserManager(self):
        
        adminBool = "Admin" if self.api.userFunctions2() else "User"
        
        if adminBool == "Admin":
            self.usermanager = UserManagerWidgetHandler()
            self.usermanager.show()
        else:
            msg_box = qtw.QMessageBox(self)
            msg_box.setWindowTitle("Access Denied")
            msg_box.setText("Restricted to Admin use only")
            msg_box.exec_()

    def disabledMenu(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Navigation Feature")
        msg_box.setText("This feature will be made available in future renditions of the software. A demonstration of the use of the toolbar is shown with the 'About' screen.")
        msg_box.exec_()

    #Data Refresh for the main Screen
    def MainWindowGUIRefresh(self):
        if self.keepRefreshing:
            print("Refreshing the GUI...")
            #Call the functions here that are responsible for performing the GUI updates...
            self.KPIMethod()  # Example update
            self.prod_data()  # Example update
            #threading.Timer(1, self.MainWindowGUIRefresh).start()
            

    def closeEvent(self, event):
        """Stop the timer when the user closes the program."""
        print("Stopping the timer...")
        self.keepRefreshing = False  # Prevent new timers from starting
        event.accept()  # Allow the program to close
        
    
# Widget execution code
if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = MainWindow()
    widget.show()

    app.exec()



