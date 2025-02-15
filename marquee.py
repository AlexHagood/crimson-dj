from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer, QRect
import sys
from PyQt6.QtGui import QPainter

class MarqueeLabel(QLabel):
    def __init__(self, text, parent=None, width=400):
        super().__init__(text, parent)

        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.setMarqueeText(text)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scrollText)
        self.timer.start(5)  # Adjust the speed of scrolling
        self.offset = 0
        self.setStyleSheet("background-color: black;color: green;")
        self.setFixedWidth(width)

    def scrollText(self):
        self.offset += 1
        if self.offset >= self.fontMetrics().horizontalAdvance(self.text()):
            self.offset = 0

        self.update()

    def setMarqueeText(self, text):
        self.setText(text.upper() + " " * 10)

        print(self.text()) 

    def paintEvent(self, event):
        painter = QPainter(self)
        textWidth = self.fontMetrics().horizontalAdvance(self.text())
        widgetWidth = self.width()
        textRect = QRect(0, 0, textWidth, self.height())
        textRect.moveLeft(-self.offset)
        painter.drawText(textRect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, self.text())

        # Draw the text again at the right edge to create the continuous effect
        if textWidth > widgetWidth:
            if self.offset > textWidth:
                self.offset = 0
            if self.offset > 0:
                textRect.moveLeft(textWidth - self.offset)
                painter.drawText(textRect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter, self.text())

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    
    marquee = MarqueeLabel("This is a scrolling marquee text example.")
    marquee.setFixedSize(400, 50)  # Set the size of the marquee label
    
    layout.addWidget(marquee)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())