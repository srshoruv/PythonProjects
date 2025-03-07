from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout

# main objects
buttonList = ['1','2','3','+','4','5','6','-','7','8','9','*','0','.','=','/']
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("iCalculator")
main_window.resize(250,300)
grid = QGridLayout()

def button_click():
    button = app.sender()
    text = button.text()

    if text == '=':
        symbol = text_box.text()
        try:
            res = eval(symbol)
            text_box.setText(str(res))
        except ZeroDivisionError:
            text_box.setText("Error")
        except NameError:
            text_box.clear()

    elif text == "Clear":
        text_box.clear()
    
    elif text == '<':
        current_text = text_box.text()
        text_box.setText(current_text[:-1])
    else:
        print("Pressed", button)
        current_text = text_box.text()
        text_box.setText(current_text + text)



row = 0
col = 0

for buttons in buttonList:
    button = QPushButton(buttons)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)

    col += 1
    if col > 3:
        row += 1
        col = 0

# creating elements
text_box = QLineEdit()
clear = QPushButton("Clear")
delete = QPushButton("<")

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

# Adding Elements
master_Layout = QVBoxLayout()
master_Layout.addWidget(text_box)
master_Layout.addLayout(grid)
master_Layout.addLayout(button_row)
main_window.setLayout(master_Layout)

# Show/hide App
clear.clicked.connect(button_click)
delete.clicked.connect(button_click)
main_window.show()
app.exec_()