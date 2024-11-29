from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc
# import secondary widget handlers
# from CustomerData_Handler? import CustomerManagerWidgetHandler? (Handler not created yet)
from OperatorManagerWidget_Handler import OperatorManagerWidgetHandler
# from <> import <> (can't find modify schedule UI file)
# from <> import <> (can't find view schedule UI file)

class ProductionScheduleManagerWidgetHandler(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_productionSchedulerWiget()
        self.ui.setupUi(self)

        # self.ui.sManagerCustomerManagerButton.clicked.connect(self.customerManagerButtonClicked)
        self.ui.sManagerOperatorManagerButton.clicked.connect(self.operatorManagerButtonClicked)
        # modify schedule button clicked (UI not created yet)
        # self.ui.pushButton.clicked.connect(self.modifyScheduleButtonClicked)
        # # view schedule button clicked (UI not created yet)
        # self.ui.pushButton_2.clicked.connect(self.viewScheduleButtonClicked)

    # def customerManagerButtonClicked(self):
    #     self. = <> ()
    #     self.<>.show()

    def operatorManagerButtonClicked(self):
        self.addNewOperatorWidget = OperatorManagerWidgetHandler()
        self.addNewOperatorWidget.show()

    # def modifyScheduleButtonClicked(self):
    #     self.editOperatorWidget = <>()
    #     self.editOperatorWidget.show()

    # def viewScheduleButtonClicked(self):
    #     self.editOperatorWidget = <>()
    #     self.editOperatorWidget.show()

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ProductionScheduleManagerWidgetHandler()
    widget.show()
    app.exec()