from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.ViewScheduleWidget_Handler import ViewScheudleWidgetHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = ViewScheudleWidgetHandler()
widget.show()
app.exec()