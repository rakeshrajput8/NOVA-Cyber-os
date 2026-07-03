import cv2


class HandScanner:

    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def read(self):

        ok, frame = self.cap.read()

        if ok:
            frame = cv2.flip(frame, 1)

        return ok, frame

    def release(self):

        if self.cap.isOpened():
            self.cap.release()