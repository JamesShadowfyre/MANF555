from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.DeleteOperatorWidget_Handler import DeleteOperatorWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = DeleteOperatorWidgetHandler()
widget.show()
app.exec()