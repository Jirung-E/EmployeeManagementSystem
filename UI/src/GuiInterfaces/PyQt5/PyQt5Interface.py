import sys

from PyQt5.QtWidgets import *

from GuiController.GuiInterface import GuiInterface


class PyQt5Interface(GuiInterface):
    def __init__(self):
        self.app = QApplication(sys.argv)

    def run(self, window):
        window.show()
        self.app.exec_()