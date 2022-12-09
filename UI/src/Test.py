import sys

from PyQt5.QtWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.isTrue = False
        self.button = QPushButton("Button", self)
        self.button.clicked.connect(self.hello)

    def hello(self):
        print("Hello")

    def show(self):
        if self.isTrue is True:
            print("True")
        else:
            print("False")
        super().show()
        
        


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()