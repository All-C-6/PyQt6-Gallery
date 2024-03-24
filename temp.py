import sys
import os
import cv2
import numpy as np
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QColor


class ImageGalleryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Gallery App")
        self.layout = QVBoxLayout(self)
        self.current_index = 0
        self.image_paths = [f"pic/{img}" for img in os.listdir("pic") if img.endswith(('.jpg', '.png', '.jpeg'))]
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)
        self.load_image()

    def load_image(self):
        image_path = self.image_paths[self.current_index]

        image = cv2.imread(image_path)
        avg_color = np.mean(image, axis=(0, 1)).astype(int)
        background_color = QColor(*avg_color)
        self.setStyleSheet(f"background-color: {background_color.name()}")

        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaledToWidth(800))
        self.setWindowTitle(f"Image Gallery App - {image_path}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Left:
            self.current_index = (self.current_index - 1) % len(self.image_paths)
            self.load_image()
        elif event.key() == Qt.Key.Key_Right:
            self.current_index = (self.current_index + 1) % len(self.image_paths)
            self.load_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gallery_app = ImageGalleryApp()
    gallery_app.show()
    sys.exit(app.exec())