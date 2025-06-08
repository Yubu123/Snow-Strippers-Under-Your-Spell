from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
import pygame
import sys

class TimedMessageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snow Strippers-Under Your Spell")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("underyspell.png"))
        pygame.mixer.init()
        pygame.mixer.music.load("undery.mp3")
        pygame.mixer.music.play(loops=-1)


        self.label = QLabel("", self)
        self.label.setStyleSheet("font-size: 30px;"
                                 "font-family:Ariel;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)
        QTimer.singleShot(000, lambda: self.label.setText("Oh-"))
        QTimer.singleShot(500, lambda: self.label.setText("Oh-oh"))
        QTimer.singleShot(1400, lambda: self.label.setText("Ah-ah"))
        QTimer.singleShot(2900, lambda: self.label.setText("Uh-ah"))
        QTimer.singleShot(4700, lambda: self.label.setText("Ah-ah"))
        QTimer.singleShot(5400, lambda: self.label.setText("They're"))
        QTimer.singleShot(5600, lambda: self.label.setText("They're permanent"))
        QTimer.singleShot(6000, lambda: self.label.setText("They're permanent, and"))
        QTimer.singleShot(6300, lambda: self.label.setText("They're permanent, and I'm"))
        QTimer.singleShot(6500, lambda: self.label.setText("They're permanent, and I'm not"))
        QTimer.singleShot(7000, lambda: self.label.setText("You"))
        QTimer.singleShot(7200, lambda: self.label.setText("You keep me"))
        QTimer.singleShot(7500, lambda: self.label.setText("You keep me under your"))
        QTimer.singleShot(7900, lambda: self.label.setText("You keep me under your spell"))
        QTimer.singleShot(8600, lambda: self.label.setText("It's"))
        QTimer.singleShot(8900, lambda: self.label.setText("It's like"))
        QTimer.singleShot(9100, lambda: self.label.setText("It's like I waited"))
        QTimer.singleShot(9500, lambda: self.label.setText("It's like I waited too long"))
        QTimer.singleShot(10300, lambda: self.label.setText("But"))
        QTimer.singleShot(10600, lambda: self.label.setText("But all the"))
        QTimer.singleShot(10900, lambda: self.label.setText("But all the scars"))
        QTimer.singleShot(11100, lambda: self.label.setText("But all the scars you can see"))
        QTimer.singleShot(12000, lambda: self.label.setText("They"))
        QTimer.singleShot(12400, lambda: self.label.setText("They are permanent"))
        QTimer.singleShot(12700, lambda: self.label.setText("And"))
        QTimer.singleShot(12900, lambda: self.label.setText("And I'm"))
        QTimer.singleShot(13100, lambda: self.label.setText("And I'm not"))
        QTimer.singleShot(13700, lambda: self.label.setText("I"))
        QTimer.singleShot(13900, lambda: self.label.setText("I want an"))
        QTimer.singleShot(14100, lambda: self.label.setText("I want an innocent"))
        QTimer.singleShot(14400, lambda: self.label.setText("I want an innocent love"))
        QTimer.singleShot(16000, lambda: self.label.setText("The rest"))
        QTimer.singleShot(16300, lambda: self.label.setText("The rest of time"))
        QTimer.singleShot(17200, lambda: self.label.setText("But"))
        QTimer.singleShot(17600, lambda: self.label.setText("But all the"))
        QTimer.singleShot(17900, lambda: self.label.setText("But all the scars"))
        QTimer.singleShot(18100, lambda: self.label.setText("You"))
        QTimer.singleShot(18400, lambda: self.label.setText("You can see"))
        QTimer.singleShot(19100, lambda: self.label.setText("When"))
        QTimer.singleShot(19400, lambda: self.label.setText("When I take"))
        QTimer.singleShot(19900, lambda: self.label.setText("When I take my clothes"))
        QTimer.singleShot(20500, lambda: self.label.setText("Off"))


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimedMessageApp()
    window.show()
    sys.exit(app.exec_())



