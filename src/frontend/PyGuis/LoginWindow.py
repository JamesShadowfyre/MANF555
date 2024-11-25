from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(699, 459)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWindow.sizePolicy().hasHeightForWidth())
        loginWindow.setSizePolicy(sizePolicy)
        loginWindow.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(loginWindow)
        self.label.setGeometry(QtCore.QRect(40, 310, 55, 16))
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(loginWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 280, 71, 16))
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.usernameInput = QtWidgets.QLineEdit(loginWindow)
        self.usernameInput.setGeometry(QtCore.QRect(130, 280, 113, 22))
        self.usernameInput.setObjectName("usernameInput")
        self.passwordInput = QtWidgets.QLineEdit(loginWindow)
        self.passwordInput.setGeometry(QtCore.QRect(130, 310, 113, 22))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.loginButton = QtWidgets.QPushButton(loginWindow)
        self.loginButton.setGeometry(QtCore.QRect(150, 360, 75, 31))
        self.loginButton.setObjectName("loginButton")
        self.forgotPasswordButton = QtWidgets.QPushButton(loginWindow)
        self.forgotPasswordButton.setGeometry(QtCore.QRect(110, 400, 151, 31))
        self.forgotPasswordButton.setObjectName("forgotPasswordButton")
        self.BackgroundPhoto = QtWidgets.QLabel(loginWindow)
        self.BackgroundPhoto.setGeometry(QtCore.QRect(0, 0, 701, 461))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackgroundPhoto.sizePolicy().hasHeightForWidth())
        self.BackgroundPhoto.setSizePolicy(sizePolicy)
        self.BackgroundPhoto.setText("")
        self.BackgroundPhoto.setPixmap(QtGui.QPixmap(r"src/frontend/PyGUIs/JonGUIs/LoginPhoto.jpg"))
        self.BackgroundPhoto.setScaledContents(True)
        self.BackgroundPhoto.setObjectName("BackgroundPhoto")
        self.label_3 = QtWidgets.QLabel(loginWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 301, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.BackgroundPhoto.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.usernameInput.raise_()
        self.passwordInput.raise_()
        self.loginButton.raise_()
        self.forgotPasswordButton.raise_()
        self.label_3.raise_()

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.label.setText(_translate("loginWindow", "Password"))
        self.label_2.setText(_translate("loginWindow", "Username"))
        self.loginButton.setText(_translate("loginWindow", "Login"))
        self.forgotPasswordButton.setText(_translate("loginWindow", "Forgot Password?"))
        self.label_3.setText(_translate("loginWindow", "Gateways MES"))