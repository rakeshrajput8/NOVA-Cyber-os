from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import QTimer

class TerminalWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setStyleSheet("""
            background-color:black;
            color:#00ff66;
            border:none;
            font-family:Consolas;
            font-size:14px;
        """)

        self.lines = [
            "[ OK ] Initializing NOVA AI...",
            "[ OK ] Loading Security Module...",
            "[ OK ] Checking CPU...",
            "[ OK ] Checking RAM...",
            "[ OK ] Camera Ready...",
            "[ OK ] Internet Connected...",
            "[ OK ] Awaiting Hand Scan..."
        ]

        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.write_line)
        self.timer.start(700)

    def write_line(self):

        if self.index < len(self.lines):

            self.append(self.lines[self.index])

            self.index += 1