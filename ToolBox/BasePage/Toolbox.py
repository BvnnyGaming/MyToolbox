from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget

import sys
from random import choice

windowTitles = [
    'Title one!',
    'Title two!',
    'Title two?',
    'title three',
    'uh oh'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #variables
        self.nTimesClicked = 0

        #page stuffs
        self.setWindowTitle("The Toolbox")

        self.setFixedSize(500, 300)

        self.label = QLabel()
        self.lineEdit = QLineEdit()

        #connecting slots
        self.lineEdit.textEdited.connect(self.label.setText)

        #layout stuffs
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

#Application Launch
app = QApplication(sys.argv)

window = MainWindow()  
window.show()

app.exec()