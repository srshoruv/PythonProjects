from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QComboBox, QLabel

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQT")

master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

button1 = QPushButton("Select Folder")
folder_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_mirror = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_gray = QPushButton("B/W")
btn_saturation = QPushButton("Saturation")
btn_contrast = QPushButton("Contrast")
btn_blur = QPushButton("Blur")

filter_box = QComboBox()
filter_box.addItems(["Original","Left", "Right","Mirror","Sharpness","B/W","Saturation","Contrast","Blur"])
picture_box = QLabel("Picture Will Appear Here")


col1.addWidget(button1)
col1.addWidget(folder_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(btn_mirror)
col1.addWidget(btn_sharp)
col1.addWidget(btn_gray)
col1.addWidget(btn_saturation)
col1.addWidget(btn_contrast)
col1.addWidget(btn_blur)
col2.addWidget(picture_box)
master_layout.addLayout(col1,20)
master_layout.addLayout(col2, 80)
main_window.setLayout(master_layout)

main_window.show()
app.exec_()