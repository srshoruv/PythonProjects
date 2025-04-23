import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QComboBox, QLabel
from PyQt5.QtGui import QPixmap

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQT")

master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

btn_folder = QPushButton("Select Folder")
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


col1.addWidget(btn_folder)
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

# App Functionality

working_directory = ""

# Filter Files and Extensions

def filter(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results


# choose current work directory

def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = ['.png', '.jpg', '.svg', '.jpeg']
    filenames = filter(os.listdir(working_directory),extensions)
    folder_list.clear()

    for filename in filenames:
        folder_list.addItem(filename)

btn_folder.clicked.connect(getWorkDirectory)



main_window.show()
app.exec_()