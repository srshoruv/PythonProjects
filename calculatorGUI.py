from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        # main objects
        self.buttonList = ['1','2','3','+','4','5','6','-','7','8','9','*','0','.','=','/']
        self.setWindowTitle("iCalculator")
        self.resize(250,300)
        self.grid = QGridLayout()
        row = 0
        col = 0

        for buttons in self.buttonList:
            button = QPushButton(buttons)
            button.setStyleSheet("QPushButton { font : 24pt Roboto; Padding: 5}")
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)

            col += 1
            if col > 3:
                row += 1
                col = 0
        # creating elements
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Roboto", 30))
        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton { font : 24pt Roboto; Padding: 5; background-color: red}")
        self.delete.setStyleSheet("QPushButton { font : 24pt Roboto; Padding: 5; background-color: Green}")

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        # Adding Elements
        master_Layout = QVBoxLayout()
        master_Layout.addWidget(self.text_box)
        master_Layout.addLayout(self.grid)
        master_Layout.addLayout(button_row)
        self.setLayout(master_Layout)

    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == '=':
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except ZeroDivisionError:
                self.text_box.setText("Error")
            except NameError:
                self.text_box.clear()

        elif text == "Clear":
            self.text_box.clear()
        
        elif text == '<':
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        else:
            print("Pressed", button)
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)
        


    
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)
        
# Show/hide App
app = QApplication([])
main_window = CalcApp()
main_window.setStyleSheet("QWidget {background-color: system}")
main_window.show()
app.exec_()