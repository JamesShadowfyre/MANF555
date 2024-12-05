from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.CreateWorkOrderWidget_Handler import CreateNewWorkOrderHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = CreateNewWorkOrderHandler()
widget.show()
app.exec()