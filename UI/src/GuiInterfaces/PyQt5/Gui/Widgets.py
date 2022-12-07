from abc import ABC, abstractmethod

import Gui.Widgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


class QtButton(Gui.Widgets.Button):
    def __init__(self):
        self.origin: QWidget

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


class QtLineEdit(Gui.Widgets.LineEdit):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__()
        self.textboxes = [ window.findChild(QLineEdit, name) ]

    def setText(self, text: str):
        self.origin.setText(text)
        
    def setEditable(self, flag: bool):
        self.origin.setReadOnly(not flag)

        if isinstance(self.origin, list):
            for e in self.origin:
                if flag is False:
                    e.setColor(Qt.lightGray)
                else:
                    e.setColor(Qt.white)
        else:
            if flag is False:
                self.setColor(Qt.lightGray)
            else:
                self.setColor(Qt.white)


class QtCombobox(Gui.Widgets.Combobox):
    def __init__(self, window: QMainWindow, name: str):
        self.origin = window.findChild(name)

    def setText(self, text: str):
        self.origin.setCurrentText(text)

    def setEditable(self, flag: bool):
        self.setEnabled(~flag)


if __name__ == "__main__":
    pass