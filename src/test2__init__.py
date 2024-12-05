from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.ProductionScheduleManagerWidget_Handler import ProductionScheduleManagerWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = ProductionScheduleManagerWidgetHandler()
widget.show()
app.exec()