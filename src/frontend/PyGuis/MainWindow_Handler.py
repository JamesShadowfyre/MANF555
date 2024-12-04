#MainWindow_Handler
from frontend.PyGuis.MainWindow import Ui_MainWindow
from frontend.PyGuis.WorkOrderManagerHome_Handler import WorkOrderManagerHomeHandler
from frontend.PyGuis.ProductionSystemsManagerWidget_Handler import ExecuteProductionWidgetHandler
from frontend.PyGuis.ProductionScheduleManagerWidget_Handler import ProductionScheduleManagerWidgetHandler
from frontend.PyGuis.InventoryManager_Handler import inventoryManagerHandler
from frontend.PyGuis.AboutWidget_Handler import AboutWidgetHandler
from backend.apiAccessPoint import ApplicationHome
# from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.api = ApplicationHome()
        self.ui.setupUi(self)
        self.keepRefreshing = True
        self.MainWindowGUIRefresh()
        
        self.MainScreenData(45, 20, 40)

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
        self.ui.actionAbout.triggered.connect(self.openAbout)
        self.ui.actionAdd_Inventory.triggered.connect(self.disabledMenu)
        self.ui.actionAdd_New_Customer.triggered.connect(self.disabledMenu)
        self.ui.actionAdd_New_Operator.triggered.connect(self.disabledMenu)
        self.ui.actionCustomers.triggered.connect(self.disabledMenu)
        self.ui.actionAdd_Inventory.triggered.connect(self.disabledMenu)
        self.ui.actionExit.triggered.connect(self.ExitFunction)
        self.ui.actionFacility_Overview.triggered.connect(self.openFactoryManagerTab)
        self.ui.actionMetrics.triggered.connect(self.disabledMenu)
        self.ui.actionNew_Work_Order.triggered.connect(self.disabledMenu)
        self.ui.actionFull_Window.triggered.connect(self.disabledMenu)
        self.ui.actionMinimize.triggered.connect(self.disabledMenu)
        self.ui.actionView_Operators.triggered.connect(self.disabledMenu)
        self.ui.actionView_Work_Orders.triggered.connect(self.disabledMenu)
        self.ui.actionView_Inventory.triggered.connect(self.disabledMenu)
        self.ui.actionTutorials.triggered.connect(self.disabledMenu)
        self.ui.actionSign_Out.triggered.connect(self.disabledMenu)
        self.ui.actionScheduler.triggered.connect(self.openProductionSchedulerTab)


    ### Updating the visual elements on the screen with data 

    def MainScreenData(self,OEE,FPFY,TSP):
        pass
        #KPIs
        self.KPIMethod()
        self.ui.OEEValue.display(OEE)
        self.ui.FPFYValue.display(FPFY)
        self.ui.TSP_Value.display(TSP)
        self.ui.userIdTextBrowser.setText(self.api.userFunctions('get'))


    def KPIMethod(self):
        OEE = 1
        FPFY = 2
        TSP = 3
        

    










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
        self.openFactory = ExecuteProductionWidgetHandler()
        self.openFactory.show()

    def openInventoryManagerTab(self):
        self.invmanage = inventoryManagerHandler()
        self.invmanage.show()
    
    def openProductionSchedulerTab(self):
        self.prodsched = ProductionScheduleManagerWidgetHandler()
        self.prodsched.show()

    def disabledMenu(self):
        msg_box = qtw.QMessageBox(self)
        msg_box.setWindowTitle("Navigation Feature")
        msg_box.setText("This feature will be made available in future renditions of the software. A demonstration of the use of the toolbar is shown with the 'About' screen.")
        msg_box.exec_()



    #Data Refresh for the main Screen
    def MainWindowGUIRefresh(self):
        if self.keepRefreshing:
            print("Refreshing the GUI...")
            #threading.Timer(1, self.MainWindowGUIRefresh).start()
            #Call the functions here that are responsible for performing the GUI updates...

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



