from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.PerformCycleCounts_Handler import updateInventoryHandler
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = updateInventoryHandler()
widget.show()
app.exec()