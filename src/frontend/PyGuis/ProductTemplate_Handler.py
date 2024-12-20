#Product Template Widget handler

#New User Widget handler
#Successfully can access the information entered by the user... only update required is to add save directories to SQL table for the 4 pieces of info

from frontend.PyGuis.CreateWorkOrderWidget_Handler import CreateNewWorkOrderHandler
from frontend.PyGuis.ProductTemplate import Ui_ProductTemplateWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class ProductTemplateHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProductTemplateWidget()
        self.ui.setupUi(self)

        self.CreateWOPassings = CreateNewWorkOrderHandler()
        
        self.BackCaseSelection = None
        self.taskCode = None
        self.DrillingAssignment = None
        self.ui.comboBox_2.addItems(["", "No drilling", "2x back holes", "2x front holes", "4x holes (2x front + 2x back)"])
        self.ui.backCaseComboBox.addItems(["","Black"])
  
        self.ui.productTemplateSave.clicked.connect(self.SaveNewTemplateWODate)

        #Drilling station is the only station that's setup, disabling all others except for case selection
        self.ui.checkBox_3.setDisabled(True)
        self.ui.checkBox_4.setEnabled(True)
        self.ui.checkBox_5.setEnabled(True) 
        self.ui.checkBox_6.setDisabled(True)
        self.ui.checkBox_7.setDisabled(True)
        self.ui.checkBox_8.setDisabled(True)
        self.ui.checkBox_9.setDisabled(True)
        self.ui.checkBox_10.setDisabled(True)
        self.ui.comboBox.setDisabled(True)
        self.ui.comboBox_3.setDisabled(True)
        self.ui.comboBox_4.setDisabled(True)
        self.ui.comboBox_5.setDisabled(True)
        self.ui.comboBox_6.setDisabled(True)
        self.ui.comboBox_7.setDisabled(True)
        self.ui.comboBox_2.setEnabled(True)
        self.ui.backCaseComboBox.setEnabled(True)
        self.ui.comboBox_2.setEnabled(True)

        #making the checkboxes function
        self.ui.backCaseComboBox.currentIndexChanged.connect(self.updateCheckBox1)
        self.ui.comboBox_2.currentIndexChanged.connect(self.updateCheckBox3)

    def updateCheckBox1(self, index):
        if index > 0:
            self.ui.checkBox_4.setChecked(True)
        else:
            self.ui.checkBox_4.setChecked(False)

    def updateCheckBox3(self, index):
        if index > 0:
            self.ui.checkBox_5.setChecked(True)
        else:
            self.ui.checkBox_5.setChecked(False)
    
    def SaveNewTemplateWODate(self):
        if self.ui.backCaseComboBox.currentIndex() <= 0 or self.ui.comboBox_2.currentIndex() <= 0:
            print("A box was not selected")
            qtw.QMessageBox.information(self,"Error", "One or more datafields were not selected. Ensure each datafield is complete.")
        
        else:
            self.DrillingArrangement = self.ui.comboBox_2.currentText()
            self.BackCaseSelection = self.ui.backCaseComboBox.currentText()
            self.ProductTemplateReturn()
            self.close()
            return self.taskCode, self.BackCaseSelection
            
    def ProductTemplateReturn(self):

        if self.DrillingArrangement == "No drilling":
            self.taskCode = 0
        elif self.DrillingArrangement == "2x back holes":
            self.taskCode = 1
        elif self.DrillingArrangement == "2x front holes":
            self.taskCode = 2
        elif self.DrillingArrangement == "4x holes (2x front + 2x back)":
            self.taskCode = 3
               

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ProductTemplateHandler()
    widget.show()
    app.exec()
