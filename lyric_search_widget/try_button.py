from PyQt6.QtWidgets import (
      QApplication, QVBoxLayout, QWidget, QLabel, QPushButton,
       QLineEdit, QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys
 
class Window(QWidget):
    def __init__(self):
        self.resources = "lyric_search_widget/resources/"
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Lyric Search Widget")
        self.setWindowIcon(QIcon(self.resources+"icon.png"))
 
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.label = QLabel("Old Text")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.adjustSize()
        layout.addWidget(self.label)

        self.input = QLineEdit(self)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
        #self.input.setPlaceholderText("format like: Artist, Title")
        #self.input = QTextEdit("try")
        #layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
 
        button = QPushButton("Update Text")
        button.clicked.connect(self.update)
        layout.addWidget(button)
 
        button = QPushButton("Print Text")
        button.clicked.connect(self.get)
        button.setIcon(QIcon(self.resources+"icon.png"))
        layout.addWidget(button)
 
    def update(self):
        self.label.setText("New and Updated Text")
     
    def get(self):
        print(self.label.text())
        text = self.input.text()
        artist = text.split()[0]
        #artist.pop[-1]
        title = text.split()[1]
        
        print(artist)
        print(title)
         
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())