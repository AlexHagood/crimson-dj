from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from marquee import MarqueeLabel
import sys

class App(QMainWindow):

    pauseState = False

    def __init__(self, image_path):
        super().__init__()



        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Load the image
        self.image_label = QLabel(central_widget)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.img_width = pixmap.width()
        self.img_height = pixmap.height()
        # Buttons
        exitButton = QPushButton("Quit", central_widget)
        exitButton.setFixedSize(50, 60)
        pauseButton = QPushButton("\u23F5", central_widget)
        self.pb = pauseButton
        pauseButton.setFixedSize(50, 60)

        exitButton.clicked.connect(self.quitApp)
        pauseButton.clicked.connect(self.pauseButton)

        exitButton.setFont(QFont('Arial', 15))

        exitButton.move(int(self.img_width * .4)  , int(self.img_height * .567) )
        pauseButton.move(int(self.img_width * .4 + 50)  , int(self.img_height * .567) )

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setGeometry(100, 100, self.img_width, self.img_height)

        # Marquee
        self.marquee_label = MarqueeLabel("Now playing: running in the 90s", central_widget, width=int(self.img_width * .8))
        self.marquee_label.setFont(QFont('Arial', 30))
        self.marquee_label.move(50, int(self.img_height*.7))
        self.marquee_label.show()

    def quitApp(self):
        self.close()
        exit()

    def pauseButton(self):
        self.pauseState = not self.pauseState
        self.pb.setText({True: "\u23F5", False: "\u23F8"}[self.pauseState])
        self.marquee_label.setMarqueeText("Now Playing:")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_path = "img/dj.png"  # Change to your image file path
    window = App(image_path)
    window.show()
    sys.exit(app.exec())