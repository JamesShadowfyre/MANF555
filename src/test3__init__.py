from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.ExecuteProductionWidget_HandlerV2 import ExecuteProductionWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = ExecuteProductionWidgetHandler()
widget.show()
app.exec()