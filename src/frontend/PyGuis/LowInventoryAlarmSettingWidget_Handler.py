#LowInventoryAlarmSettingWidget_Handler


from frontend.PyGuis.LowInventoryAlarmSettingWidget import Ui_lowInventoryAlarmSettingsWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class LowInventoryAlarmWidget(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_lowInventoryAlarmSettingsWidget()
        self.ui.setupUi(self)

        #-----------------------------------------------------
        #James: 
        # read the "low inventory alarm setting" from the database - lowInvDataRead [int]
        # 
        #-----------------------------------------------------
        lowInvDataRead = 8
        self.ui.lineEdit.setText(str(lowInvDataRead)) #This will need to be changed to a string from the actual database value
        self.ui.lineEdit.setDisabled(True)

        self.ui.pushButton.clicked.connect(self.SaveNewInvAlarmSetpoint)

    def SaveNewInvAlarmSetpoint(self):
        LowInvDataWrite = int(self.ui.lowInventorySetInput.value()) #change LHS to SQL table reference
        qtw.QMessageBox.information(self, "Low Inventory Limit", "Low Inventory Limit updated.")
        
        DATAENTRY = LowInvDataWrite
        #-----------------------------------------------------
        #James: 
        # write the "low inventory alarm setting" to LowInvDataWrite - writes as integer
        # 
        #-----------------------------------------------------

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = LowInventoryAlarmWidget()
    widget.show()
    app.exec()
