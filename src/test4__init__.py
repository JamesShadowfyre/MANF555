from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.RecieveInventoryWidget_Handler import RecieveInventoryWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = RecieveInventoryWidgetHandler()
widget.show()
app.exec()