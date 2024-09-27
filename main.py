import sys

from PyQt6.QtWidgets import QApplication

from src.widgets.main_window import WindowMain


def application():
    """main func for run application"""
    app = QApplication(sys.argv)
    window = WindowMain()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
