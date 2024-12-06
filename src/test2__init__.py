from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.AddNewOperatorWidget_Handler import AddNewOperatorHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = AddNewOperatorHandler()
widget.show()
app.exec()