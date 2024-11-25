from TaskCodeSelection import Ui_Form
from variables import TaskCode

class TaskCodeSelection_Handler (qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.taskCodeSlider.valueChanged.connect(self.updateValue)

    def updateValue (value): 
        global TaskCode
        TaskCode = value 
