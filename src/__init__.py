from backend.apiAccessPoint import ApplicationHome
from frontend.PyGuis.LoginWindow_Handler import loginWindowHandler
from PyQt5 import QtWidgets as qtw
import atexit

api = ApplicationHome()
api.init_app()
app = qtw.QApplication([])
widget = loginWindowHandler()
widget.show()
app.exec()
def exitHandler():
    for workOrder in list(api.workOrderMap.values()):
        workOrder.disconnect()
        
atexit.register(exitHandler())
    
