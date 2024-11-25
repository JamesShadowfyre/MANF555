from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

# Screen 1
class Screen1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screen 1")
        layout = QVBoxLayout()
        button = QPushButton("Go to Screen 2")
        layout.addWidget(button)
        self.setLayout(layout)
        button.clicked.connect(self.go_to_screen2)

    def go_to_screen2(self):
        # Trigger navigation to Screen 2
        self.parent().setCurrentIndex(1)

# Screen 2
class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screen 2")
        layout = QVBoxLayout()
        button = QPushButton("Go to Screen 1")
        layout.addWidget(button)
        self.setLayout(layout)
        button.clicked.connect(self.go_to_screen1)

    def go_to_screen1(self):
        # Trigger navigation to Screen 1
        self.parent().setCurrentIndex(0)

# Main Window (Manages Navigation)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        # Create a stacked widget to manage the screen transitions
        self.stacked_widget = QStackedWidget(self)

        # Create screen widgets
        self.screen1 = Screen1()
        self.screen2 = Screen2()

        # Add screens to the stacked widget
        self.stacked_widget.addWidget(self.screen1)
        self.stacked_widget.addWidget(self.screen2)

        # Layout for the main window
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)

        self.setLayout(main_layout)

        # Show the first screen (index 0)
        self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
