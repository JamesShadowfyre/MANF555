from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.OperatorManagerWidget_Handler import OperatorManagerWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = OperatorManagerWidgetHandler()
widget.show()
app.exec()