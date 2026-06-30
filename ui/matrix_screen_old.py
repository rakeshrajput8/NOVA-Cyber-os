# ===== Laser Scan Effect =====

if not self.scan_complete:

    painter.setPen(QColor(0, 255, 120))
    painter.drawLine(
        self.camera.x(),
        self.camera.y() + self.scan_y,
        self.camera.x() + self.camera.width(),
        self.camera.y() + self.scan_y
    )

    painter.fillRect(
        self.camera.x(),
        self.camera.y() + self.scan_y - 2,
        self.camera.width(),
        4,
        QColor(0, 255, 120, 120)
    )

    self.scan_y += self.scan_speed

    self.progress = min(100, int((self.scan_y / self.camera.height()) * 100))

    painter.setFont(QFont("Consolas", 12))
    painter.setPen(QColor(0, 255, 120))

    painter.drawText(
        self.camera.x(),
        self.camera.y() + self.camera.height() + 25,
        f"SCAN {self.progress}%"
    )

    if self.scan_y >= self.camera.height():
        self.scan_complete = True

else:

    painter.setPen(QColor(0, 255, 120))
    painter.setFont(QFont("Consolas", 20, QFont.Bold))

    painter.drawText(
        self.camera.x(),
        self.camera.y() + self.camera.height() + 30,
        "ACCESS GRANTED"
    )
    # ==========================================
# PAINT EVENT
# ==========================================

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.fillRect(self.rect(), Qt.black)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.setFont(QFont("Consolas",16))

        width = max(1, self.width() // self.columns)

        for i in range(self.columns):

            char = random.choice(LETTERS)

            x = i * width

            y = self.drops[i] * 20

            glow = random.randint(150,255)

            painter.setPen(QColor(0,glow,70))

            painter.drawText(x,y,char)

            self.drops[i] += 1

            if y > self.height():

                self.drops[i] = random.randint(-30,0)

        # ==========================
        # HUD BORDER
        # ==========================

        painter.setPen(QColor(0,255,120))

        painter.drawRect(
            10,
            10,
            self.width()-20,
            self.height()-20
        )

        painter.setFont(
            QFont("Consolas",22,QFont.Bold)
        )

        painter.drawText(
            30,
            45,
            "NOVA CYBER OS"
        )

        painter.setFont(
            QFont("Consolas",12)
        )

        painter.drawText(
            30,
            70,
            "AI SECURITY ENGINE ONLINE"
        )

        painter.drawText(
            30,
            95,
            "CAMERA INITIALIZED"
        )

        painter.drawText(
            30,
            120,
            "WAITING FOR HAND SCAN..."
        )

        # ==========================
        # LASER SCAN
        # ==========================

        if not self.scan_complete:

            camx = self.camera.x()
            camy = self.camera.y()

            painter.setPen(QColor(0,255,120))

            painter.drawLine(
                camx,
                camy+self.scan_y,
                camx+self.camera.width(),
                camy+self.scan_y
            )

            painter.fillRect(
                camx,
                camy+self.scan_y-2,
                self.camera.width(),
                4,
                QColor(0,255,120,100)
            )

            self.scan_y += self.scan_speed

            self.progress = min(
                100,
                int(
                    (self.scan_y/self.camera.height())*100
                )
            )
            # ==========================================
# ACCESS GRANTED
# ==========================================

        if self.show_access:

            painter.setFont(
                QFont("Consolas", 28, QFont.Bold)
            )

            painter.setPen(QColor(0, 255, 120))

            painter.drawText(
                40,
                self.height() - 130,
                "ACCESS GRANTED"
            )

            painter.setFont(
                QFont("Consolas", 18)
            )

            painter.drawText(
                40,
                self.height() - 90,
                f"WELCOME {self.username}"
            )

            # Progress Bar
            painter.drawRect(
                40,
                self.height() - 60,
                300,
                18
            )

            painter.fillRect(
                42,
                self.height() - 58,
                self.progress * 3 - 4,
                14,
                QColor(0, 255, 120)
            )

    # ==========================================
    # CLOSE EVENT
    # ==========================================

    def closeEvent(self, event):

        if self.cap.isOpened():
            self.cap.release()

        event.accept()

# ===========================
# PART 3 END
# ===========================