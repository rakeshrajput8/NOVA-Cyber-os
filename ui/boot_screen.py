from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QProgressBar
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont


class BootScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NOVA Cyber OS")

        self.setStyleSheet("background:black;")

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)

        self.title = QLabel("NOVA CYBER OS")
        self.title.setFont(QFont("Consolas",30))
        self.title.setStyleSheet("color:#00ff66;")

        self.status = QLabel("Initializing...")
        self.status.setStyleSheet("color:white;font-size:18px;")

        self.progress = QProgressBar()
        self.progress.setMaximum(100)
        self.progress.setStyleSheet("""
        QProgressBar{
            border:2px solid #00ff66;
            color:white;
            text-align:center;
        }

        QProgressBar::chunk{
            background:#00ff66;
        }
        """)

        layout.addWidget(self.title)
        layout.addSpacing(30)
        layout.addWidget(self.status)
        layout.addWidget(self.progress)

        self.setLayout(layout)

        self.value=0

        self.timer=QTimer()

        self.timer.timeout.connect(self.update_progress)

        self.timer.start(40)

    def update_progress(self):

        self.value+=1

        self.progress.setValue(self.value)

        if self.value<25:
            self.status.setText("Initializing AI Core...")

        elif self.value<50:
            self.status.setText("Loading Security...")

        elif self.value<75:
            self.status.setText("Connecting Camera...")

        elif self.value<100:
            self.status.setText("Launching NOVA...")

        else:
            self.status.setText("SYSTEM READY")
            self.timer.stop()