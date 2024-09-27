from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton

from src.static.window import q_main_window_style


class WindowMain(QMainWindow):
    """main window"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Learning app")
        self.setGeometry(400, 200, 400, 300)
        self.setStyleSheet(q_main_window_style)

        self.main_text = QLabel(self)
        self.main_text.setText("Hello, PyQt6!")
        self.main_text.move(160, 150)
        self.main_text.adjustSize()

        self.button = QPushButton(self)
        self.button.setText("Click me!")
        self.button.move(50, 250)
        self.button.setFixedWidth(300)
        self.button.clicked.connect(self.add_label)

    @staticmethod
    def add_label(self):
        print("Clicked!")
