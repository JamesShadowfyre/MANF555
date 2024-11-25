#Product Template Widget handler

#New User Widget handler
#Successfully can access the information entered by the user... only update required is to add save directories to SQL table for the 4 pieces of info

from ProductTemplate import Ui_ProductTemplateWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class ProductTemplateHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProductTemplateWidget()
        self.ui.setupUi(self)

        self.ui.comboBox_2.addItems([])
  
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

    def SaveNewTemplateWODate(self):
        pass
        DrillingArrangement = self.ui.comboBox_2.currentText()
        BackCaseSelection = self.ui.backCaseComboBox.currentText()

        print(DrillingArrangement)
        print(BackCaseSelection)

        self.close()

    def convertToTaskCode(self,DrillingArrangement):
        if DrillingArrangement == "No Holes":
            




if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = ProductTemplateHandler()
    widget.show()
    app.exec()
