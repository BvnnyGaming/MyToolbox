from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton
)
import sys
from apps.cardReader import ImageLoader

class Launcher(QWidget):
    def __init__(self):
        #Page details
        super().__init__()
        self.setWindowTitle("The Toolbox")
        self.setMinimumHeight("")
        self.windows = [] #For garbage collector

        #Format app button
        layout = QVBoxLayout(self)
        btn1 = QPushButton("Image Loader")
        btn1.clicked.connect(self.openImageLoader)
        layout.addWidget(btn1)

    #Open app
    def openImageLoader(self):
        win = ImageLoader()
        self.windows.append(win)
        win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())