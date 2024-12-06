from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.EditCustomerWidget_Handler import EditCustomerWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = EditCustomerWidgetHandler()
widget.show()
app.exec()