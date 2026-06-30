import sys
from PySide6.QtWidgets import QApplication
from ui.matrix_screen import MatrixScreen

app = QApplication(sys.argv)

window = MatrixScreen()
window.showFullScreen()

sys.exit(app.exec())