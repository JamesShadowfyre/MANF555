from backend.apiAccessPoint import ApplicationHome
from backend.externalCommunication.database import Database
#MainWindow_Handler
from frontend.PyGuis.LoginWindow_Handler import loginWindowHandler
# from ProductionScheduleManagerWidget import Ui_productionSchedulerWiget
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = loginWindowHandler()
widget.show()
app.exec()

