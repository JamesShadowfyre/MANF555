from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.UserManagerWidget_Handler import UserManagerWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = UserManagerWidgetHandler()
widget.show()
app.exec()