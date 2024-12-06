from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.DeleteUserWidget_Handler import DeleteWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = DeleteWidgetHandler()
widget.show()
app.exec()