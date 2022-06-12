import pyttsx3
engine = pyttsx3.init()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit

app = QApplication([])
win = QWidget()
win.setWindowTitle("мое окно")
win.move(300, 20)
win.resize(600,600)
win.show()

main_layout = QVBoxLayout()
win.setLayout(main_layout)

text = QTextEdit()
main_layout.addWidget(text)

button = QPushButton("СКАЗАТЬ")
main_layout.addWidget(button)

def say():
    text_to_say = text.toPlainText()
    engine.say(text_to_say)
    engine.runAndWait()

button.clicked.connect(say)

app.exec_()