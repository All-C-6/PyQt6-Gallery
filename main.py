import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
import os


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
        pixmap = QPixmap(self.image_paths[self.current_index])
        self.image_label.setPixmap(pixmap.scaledToWidth(800))  # Измените размер изображения по вашему усмотрению

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