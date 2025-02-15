from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer
import sys
from PyQt6.QtGui import QPainter

class MarqueeLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.setText(text)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scrollText)
        self.timer.start(10)
        self.offset = 0

    def scrollText(self):
        self.offset += 1
        if self.offset >= self.fontMetrics().horizontalAdvance(self.text()):
            self.offset = 0

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        textWidth = self.fontMetrics().horizontalAdvance(self.text())
        textRect = self.rect()
        textRect.moveLeft(-self.offset)
        painter.drawText(textRect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, self.text())

        # Draw the text again at the right edge to create the continuous effect
        if self.offset > 0:
            textRect.moveLeft(textWidth - self.offset + 100)
            painter.drawText(textRect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, self.text())

        painter.end()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    marquee = MarqueeLabel("This is a scrolling marquee text example.")
    
    layout.addWidget(marquee)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())