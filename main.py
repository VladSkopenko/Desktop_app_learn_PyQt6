import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

from src.static.window import q_main_window_style


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Learning app")
    window.setGeometry(400, 300, 300, 200)
    window.setStyleSheet(q_main_window_style)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
