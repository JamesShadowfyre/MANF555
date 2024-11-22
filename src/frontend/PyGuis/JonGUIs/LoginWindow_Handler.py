#MainWindow_Handler

from LoginWindow import Ui_loginWindow
from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtGui
from PyQt5 import QtCore as qtc

class AboutWidgetHandler(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_loginWindow()
        self.ui.setupUi(self)

        self.ui.forgotPasswordButton.clicked.connect(self.forgotPassword)

    def forgotPassword(self):
        qtw.QMessageBox.information(self,"Forgot Password", "Please contact Administrator for password reset")

if __name__ == '__main__':
    app = qtw.QApplication([])
    widget = AboutWidgetHandler()
    widget.show()
    app.exec()



