from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class FloatingImage(QLabel):

    pauseState = False;

    def __init__(self, image_path):
        super().__init__()

        # Load the image
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap)
        img_width = pixmap.width()
        img_height = pixmap.height()

        #button
        exitButton = QPushButton("Quit", self)
        exitButton.setFixedSize(50, 60)
        pauseButton = QPushButton("\u23F5", self)
        self.pb = pauseButton
        exitButton.setFixedSize(50, 60)
        pauseButton.setFixedSize(50, 60)

        exitButton.clicked.connect(self.quitApp)
        pauseButton.clicked.connect(self.pauseButton)

        exitButton.move(int(img_width * .4)  , int(img_height * .567) )
        pauseButton.move(int(img_width * .4 + 50)  , int(img_height * .567) )

        exitButton.setFont(QFont('Times', 15))
        pauseButton.setFont(QFont('Times', 15))

        # Remove window frame and make it topmost
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Set the image size
        self.resize(pixmap.size())
        self.show()
    def quitApp(self):
        self.close()
        exit()

    def pauseButton(self):
        self.pauseState = not self.pauseState
        self.pb.setText({True: "\u23F5", False: "\u23F8"}[self.pauseState])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_path = "img/dj.png"  # Change to your image file path
    floating_image = FloatingImage(image_path)
    sys.exit(app.exec())
