"""
Sources:
http://stackoverflow.com/questions/37399515/how-to-make-a-widgets-height-a-fixed-proportion-to-its-width
"""

from PyQt5.QtWidgets import QWidget, QLabel, QGraphicsView
from PyQt5.QtGui import QPixmap
import math


class PaintingView(QWidget):
    """
    Reimplementation to keep aspect ratio of widget
    """

    def __init__(self):
        super().__init__()
        painting = QPixmap('./resources/donald-trump.png')
        pixmap_size = painting.size()
        self._height_for_width_factor = 1.0 * pixmap_size.height() / pixmap_size.width()
        self._label = QLabel('pixmap', self)
        self._label.setPixmap(painting)
        self.setMinimumSize(pixmap_size)

        self._painting_graphics = QGraphicsView()

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        # we had to reimplement it to keep aspect ratio
        return math.ceil(width * self._height_for_width_factor)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._resizeImage(event.size())

    def _resizeImage(self, size):
        width = size.width()
        height = self.heightForWidth(width)
        self._label.setFixedSize(width, height)