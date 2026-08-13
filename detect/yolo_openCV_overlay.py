import sys
import cv2
import torch
import numpy as np
from mss import MSS
from ultralytics import YOLO

import win32gui
import win32con

from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget


MODEL_PATH = r"C:[input actual path]\Wildlife_Object_Detection\model\small_imageset_model\runs\detect\wildlife_yolo26n\weights\best.pt"

CAPTURE_REGION = {
    "top": 10,
    "left": 10,
    "width": 2540,
    "height": 1420,
}

CONFIDENCE = 0.75
IMG_SIZE = 416
BOX_PADDING = 8


class YoloOverlay(QWidget):
    def __init__(self):
        super().__init__()

        if not torch.cuda.is_available():
            raise RuntimeError("CUDA/GPU not available. Aborting.")

        print(f"Using GPU: {torch.cuda.get_device_name(0)}")

        self.model = YOLO(MODEL_PATH)
        self.sct = MSS()
        self.boxes = []

        self.setGeometry(
            CAPTURE_REGION["left"],
            CAPTURE_REGION["top"],
            CAPTURE_REGION["width"],
            CAPTURE_REGION["height"],
        )

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.timer = QTimer()
        self.timer.timeout.connect(self.run_detection)
        self.timer.start(200)

        self.top_timer = QTimer()
        self.top_timer.timeout.connect(self.keep_on_top)
        self.top_timer.start(1000)

    def keep_on_top(self):
        hwnd = int(self.winId())

        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE
            | win32con.SWP_NOSIZE
            | win32con.SWP_SHOWWINDOW,
        )

    def run_detection(self):
        screenshot = self.sct.grab(CAPTURE_REGION)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        results = self.model.predict(
            source=frame,
            conf=CONFIDENCE,
            imgsz=IMG_SIZE,
            device=0,
            half=True,
            verbose=False,
        )

        self.boxes = []

        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
           
            x1 = max(0, x1 - BOX_PADDING)
            y1 = max(0, y1 - BOX_PADDING)
            x2 = min(CAPTURE_REGION["width"], x2 + BOX_PADDING)
            y2 = min(CAPTURE_REGION["height"], y2 + BOX_PADDING)
           
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = self.model.names[cls_id]

            self.boxes.append({
                "rect": QRect(
                    int(x1),
                    int(y1),
                    int(x2 - x1),
                    int(y2 - y1),
                ),
                "label": f"{label} {conf:.2f}",
            })

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        outline_pen = QPen(QColor(0, 255, 0), 3)
        painter.setPen(outline_pen)
        painter.drawRect(1, 1, self.width() - 2, self.height() - 2)

        box_pen = QPen(QColor(0, 255, 0), 3)
        painter.setPen(box_pen)
        painter.setFont(QFont("Arial", 14, QFont.Bold))

        for item in self.boxes:
            rect = item["rect"]
            label = item["label"]

            painter.setPen(box_pen)
            painter.drawRect(rect)

            metrics = painter.fontMetrics()
            text_width = metrics.horizontalAdvance(label)
            text_height = metrics.height()
            padding = 6

            text_x = rect.x()
            text_y = max(text_height + padding, rect.y())

            painter.fillRect(
                text_x - padding,
                text_y - text_height,
                text_width + padding * 2,
                text_height + padding,
                QColor(255, 255, 255),
            )

            painter.setPen(QPen(QColor(0, 0, 0), 1))
            painter.drawText(text_x, text_y, label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = YoloOverlay()
    overlay.show()
    overlay.keep_on_top()
    sys.exit(app.exec_())