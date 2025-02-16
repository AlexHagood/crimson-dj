from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from marquee import MarqueeLabel
import sys

class App(QMainWindow):

    pauseState = False
    hiddenState = 1
    

    def __init__(self, image_path):
        super().__init__()



        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.dtimer = QTimer(self)
        self.dtimer.timeout.connect(self.on_timeout)


        # Load the image
        self.image_label = QLabel(central_widget)
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.img_width = pixmap.width()
        self.img_height = pixmap.height()
        # Buttons
        exitButton = QPushButton("Quit", central_widget)
        exitButton.setFixedSize(50, 60)

        dragButton = QPushButton("", central_widget)
        dragButton.setFixedSize(int(self.width() * .2), int(self.height()*.2))
        dragButton.move(int(self.width() * .51),int(self.height()*.05))
        dragButton.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")

        dragButton.pressed.connect(self.on_press)

        dragButton.setCursor(Qt.CursorShape.PointingHandCursor)


        

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

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.screen_width = screen_geometry.width()
        self.screen_height = screen_geometry.height()
        print(f"Screen width: {self.screen_width}, Screen height: {self.screen_height}")

        self.setGeometry(100, 100, self.img_width, self.screen_height - self.img_height)

        self.move(0, self.screen_height - self.img_height + 10)

        # Marquee
        self.marquee_label = MarqueeLabel("Now playing: running in the 90s", central_widget, width=int(self.img_width * .8))
        self.marquee_label.setFont(QFont('Arial', 30))
        self.marquee_label.move(50, int(self.img_height*.7))
        self.marquee_label.show()

        # Load the speech bubble image and scale it down to 0.20
        speech_bubble_path = "img/speech.png"
        speech_bubble_pixmap = QPixmap(speech_bubble_path)
        scaled_pixmap = speech_bubble_pixmap.scaled(speech_bubble_pixmap.width() // 3, speech_bubble_pixmap.height() // 5, Qt.AspectRatioMode.IgnoreAspectRatio , Qt.TransformationMode.SmoothTransformation)
        self.speech = QLabel(central_widget)
        self.speech.setPixmap(scaled_pixmap)
        self.speech.move(int(self.img_width * .1), 0)
        self.speech.hide()

        self.speechText = QLabel("Wassup dog", self.speech)
        self.speechText.setStyleSheet("color: black;")
        self.speechText.setGeometry(int(scaled_pixmap.width() * .028), int(scaled_pixmap.height() * .1), int(scaled_pixmap.width() * .94), int(scaled_pixmap.height() * .5))
        self.speechText.setFont(QFont('Courier', 20))



        self.opacity_effect = QGraphicsOpacityEffect(self.speech)
        self.speech.setGraphicsEffect(self.opacity_effect)

    def on_press(self):
        self.steps = 0
        self.dtimer.timeout.connect(self.on_timeout)
        self.inc = self.img_height // 35
        self.dtimer.start(50)

    def apply_fade_in(self, widget):
            """Applies a fade-in effect to the given widget."""
            opacity_effect = QGraphicsOpacityEffect()
            widget.setGraphicsEffect(opacity_effect)

            animation = QPropertyAnimation(opacity_effect, b"opacity")
            animation.setDuration(1000)  # 1 second
            animation.setStartValue(0)   # Fully transparent
            animation.setEndValue(1)     # Fully opaque
            animation.setEasingCurve(QEasingCurve.Type.InOutQuad)  # Smooth effect
            animation.start()

            # Keep a reference to prevent garbage collection
            self.animation = animation  


    def speak(self, text):
        self.speechText.setText(text)
        self.apply_fade_in(self.speech)
        self.speechTimer = QTimer(self)
        self.speechTimer.timeout.connect(self.hideSpeech)
        self.speechTimer.start(5000)

    def hideSpeech(self):
        self.fadeout(self.speech)
        self.speechTimer.stop()



    def on_timeout(self):
        print(f"{self.steps, self.hiddenState}")
        self.steps += 1;

        if self.steps == 30:
            self.dtimer.stop()
            self.hiddenState *= -1
            return
        elif self.steps < 30: 
            new_y = self.y() + (self.hiddenState * self.inc)
            self.setFixedHeight(self.height() - self.hiddenState * self.inc)
            self.move(self.x(), new_y)

        

        


    def quitApp(self):
        self.close()
        exit()

    def pauseButton(self):
        self.pauseState = not self.pauseState
        self.pb.setText({True: "\u23F5", False: "\u23F8"}[self.pauseState])
        self.marquee_label.setMarqueeText("Now Playing:")
        self.speak("Whatsup dog!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    image_path = "img/dj.png"  # Change to your image file path
    window = App(image_path)
    window.show()
    sys.exit(app.exec())