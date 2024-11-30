#LowInventoryAlarmSettingWidget_Handler

"""
Remaining work:
- connect newLowInvSetpoint to database value
- connect self.ui.lineEdit.setText() to use existing value from database


"""


from LowInventoryAlarmSettingWidget import Ui_lowInventoryAlarmSettingsWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class LowInventoryAlarmWidget(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_lowInventoryAlarmSettingsWidget()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText("7") #This will need to be changed to a string from the actual database value
        self.ui.lineEdit.setDisabled(True)

        self.ui.pushButton.clicked.connect(self.SaveNewInvAlarmSetpoint)

    def SaveNewInvAlarmSetpoint(self):
        newLowInvSetpoint = self.ui.lowInventorySetInput.value() #change LHS to SQL table reference
        qtw.QMessageBox.information(self, "Low Inventory Limit", "Low Inventory Limit updated.")
        print("New Inventory Alarm Threshold Setting: ",newLowInvSetpoint)

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = LowInventoryAlarmWidget()
    widget.show()
    app.exec()
