from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QColor
from PySide6.QtCore import QTimer


class TerminalWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setStyleSheet("""
            QTextEdit{
                background:black;
                color:#00ff66;
                border:2px solid #00ff66;
                font-family:Consolas;
                font-size:13px;
            }
        """)

        self.logs = [
            "[ OK ] NOVA CORE LOADED",
            "[ OK ] AI ENGINE READY",
            "[ OK ] SECURITY MODULE ONLINE",
            "[ OK ] CAMERA INITIALIZED",
            "[ OK ] TERMINAL READY",
            "[ OK ] WAITING FOR USER..."
        ]

        self.index = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_log)
        self.timer.start(900)

    def add_log(self):

        if self.index < len(self.logs):

            self.append(self.logs[self.index])

            self.index += 1