from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLayout, QLabel

import sys

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")

        self.window = QWidget
        self.setGeometry(200, 200, 520, 180)
        self.layout = QGridLayout
       
        self.window.setLayout(self.layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
