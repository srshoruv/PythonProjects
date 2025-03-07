from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
import webbrowser

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PeerSyncZ")
main_window.resize(400,400)

title = QLabel("Welcome to our app!")


row1 = QHBoxLayout()
button1 = QPushButton("Computer Fundamentals")
button2 = QPushButton("Structured Programming Language")
button3 = QPushButton("Mathematics")
button4 = QPushButton("Physics")
button5 = QPushButton("English")

master_layout = QVBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

master_layout.addLayout(row1)
master_layout.addWidget(button1, alignment=Qt.AlignCenter)
master_layout.addWidget(button2, alignment=Qt.AlignCenter)
master_layout.addWidget(button3, alignment=Qt.AlignCenter)
master_layout.addWidget(button4, alignment=Qt.AlignCenter)
master_layout.addWidget(button5, alignment=Qt.AlignCenter)

def math():
    webbrowser.open("https://drive.google.com/drive/folders/1R8KTTFcFUevUe_sMi_VWhc2uFNMPKdlr")

def computer():
    webbrowser.open("https://drive.google.com/drive/folders/1IkRBVejxkQj-iburmzpnfqJKodhTFX-k")

def spl():
    webbrowser.open("https://drive.google.com/drive/folders/1kNHZfjJbes0pJyKC47mxLpWW90R2EhIj")

def phy():
    webbrowser.open("https://drive.google.com/drive/folders/1VcLpGeLW6xM4UUJnHO830RreTP1ZxgiT")

def eng():
    webbrowser.open("https://drive.google.com/drive/folders/1M1h_eou4YPtXVSYY-feIFlXLIUC36NWf")

button1.clicked.connect(computer)
button2.clicked.connect(spl)
button3.clicked.connect(math)
button4.clicked.connect(phy)
button5.clicked.connect(eng)

main_window.setLayout(master_layout)

main_window.show()
app.exec_()