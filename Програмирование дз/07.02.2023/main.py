import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

class Buttons():

    def __init__(self, buttons: list):
        self.buttons = {}
        for button in buttons:
            self.buttons[str(str(button))] = QPushButton(str(button))

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(320, 300, 300, 100)
        self.setWindowTitle("Калькулятор")
        self.buttons = Buttons([0,1,2,3,4,5,6,7,8,9,"+","-", "="]).buttons
        self.layout = QVBoxLayout(self)
        for button in self.buttons.keys():
            self.layout.addWidget(self.buttons[button])
        #self.curbutton = button
        # self.layout.addWidget(self.buttons["="])
        #     self.buttons[str(str(button))] = QPushButton(str(button))
  #  def div(self):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

