from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.EditOperatorWidget_Handler import EditOperatorWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = EditOperatorWidgetHandler()
widget.show()
app.exec()