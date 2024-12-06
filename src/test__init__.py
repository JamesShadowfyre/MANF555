from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.MachineList_Handler import Ui_MachineList
from PyQt5 import QtWidgets as qtw


api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = Ui_MachineList()
widget.show()
app.exec()