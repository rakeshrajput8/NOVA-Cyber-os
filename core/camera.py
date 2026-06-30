import cv2
import mediapipe as mp


class HandScanner:

    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.drawer = mp.solutions.drawing_utils

        self.progress = 0
        self.scan_y = 0

    def draw_scanner(self, frame):

        self.scan_y += 5

        if self.scan_y > frame.shape[0]:
            self.scan_y = 0

        cv2.line(
            frame,
            (0, self.scan_y),
            (frame.shape[1], self.scan_y),
            (0, 255, 0),
            2
        )

    def draw_progress(self, frame):

        cv2.rectangle(
            frame,
            (20,430),
            (320,455),
            (255,255,255),
            2
        )

        cv2.rectangle(
            frame,
            (20,430),
            (20 + self.progress*3,455),
            (0,255,0),
            -1
        )

        cv2.putText(
            frame,
            f"SCAN {self.progress}%",
            (20,420),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

# ===== PART 1 END =====# ===== PART 2 START =====

    def run(self):

        while True:

            success, frame = self.cap.read()

            if not success:
                break

            frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            result = self.hands.process(rgb)

            hand_found = False

            if result.multi_hand_landmarks:

                hand_found = True

                for hand in result.multi_hand_landmarks:

                    self.drawer.draw_landmarks(
                        frame,
                        hand,
                        self.mpHands.HAND_CONNECTIONS
                    )

                if self.progress < 100:
                    self.progress += 2

            else:

                if self.progress > 0:
                    self.progress -= 2

            self.draw_scanner(frame)

            self.draw_progress(frame)

            if hand_found:

                cv2.putText(
                    frame,
                    "HAND DETECTED",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2
                )

            else:

                cv2.putText(
                    frame,
                    "PLACE YOUR HAND",
                    (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,255),
                    2
                )

# ===== PART 2 END =====# ===== PART 3 START =====

            if self.progress >= 100:

                cv2.putText(
                    frame,
                    "ACCESS GRANTED",
                    (60, 90),
                    cv2.FONT_HERSHEY_DUPLEX,
                    1.2,
                    (0, 255, 0),
                    3
                )

                cv2.putText(
                    frame,
                    "WELCOME RAKESH",
                    (60, 130),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 255),
                    2
                )

            cv2.imshow("NOVA Hand Scanner", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    scanner = HandScanner()
    scanner.run()

# ===== PART 3 END =====