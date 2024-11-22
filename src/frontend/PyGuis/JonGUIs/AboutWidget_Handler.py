#MainWindow_Handler

from AboutWidget import Ui_AboutWidget
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class AboutWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_AboutWidget()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AboutWidgetHandler()
    widget.show()
    app.exec()



