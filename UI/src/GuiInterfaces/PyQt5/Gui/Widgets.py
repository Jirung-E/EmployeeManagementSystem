from abc import ABC, abstractmethod

import Gui.Widgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


class QtButton(Gui.Widgets.Button):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__(window.findChild(QPushButton, name))

    def bindFunction(self, func: callable):
        self.origin.clicked.connect(func)

    def setText(self, text: str):
        self.origin.setText(text)
        

class QtTextbox(Gui.Widgets.Textbox):
    def __init__(self):
        self.origin: QWidget

    @abstractmethod
    def setEditable(self, flag: bool):
        pass

    @abstractmethod
    def setText(self, text: str):
        pass

    def setEnabled(self, flag: bool):
        self.origin.setEnabled(flag)

    def setColor(self, color: Qt.GlobalColor):
        palette = QPalette()
        palette.setColor(QPalette.Base, color)
        self.origin.setPalette(palette)


class QtLineEdit(Gui.Widgets.LineEdit, QtTextbox):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__(name)
        self.origin = window.findChild(QLineEdit, name)

    def setText(self, text: str):
        self.origin.setText(text)
        
    def setEditable(self, flag: bool):
        self.origin.setReadOnly(not flag)

        if flag is False:
            self.setColor(Qt.lightGray)
        else:
            self.setColor(Qt.white)


class QtCombobox(Gui.Widgets.Combobox, QtTextbox):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__(name)
        self.origin = window.findChild(name)

    def setText(self, text: str):
        self.origin.setCurrentText(text)

    def setEditable(self, flag: bool):
        self.setEnabled(~flag)


if __name__ == "__main__":
    pass