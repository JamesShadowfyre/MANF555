from backend.apiAccessPoint import ApplicationHome
#MainWindow_Handler
from frontend.PyGuis.MainWindow_Handler import MainWindow
# from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = MainWindow()
widget.show()
app.exec()

    