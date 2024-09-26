import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Train app")
    window.setGeometry(400, 300, 300, 200)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
