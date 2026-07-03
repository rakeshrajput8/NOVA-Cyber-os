import sys

from PySide6.QtWidgets import QApplication
from ui.matrix_screen import MatrixScreen


def main():
    app = QApplication(sys.argv)

    window = MatrixScreen()
    window.showFullScreen()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()