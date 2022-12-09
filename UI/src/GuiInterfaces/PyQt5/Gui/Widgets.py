from abc import abstractmethod

import Gui.Widgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class QtWidget(Gui.Widgets.Widget):
    def __init__(self, origin: QWidget):
        super().__init__(origin)

    def setEnabled(self, flag: bool):
        self.origin.setEnabled(flag)
        
    def setHidden(self, flag: bool):
        self.origin.setHidden(flag)


class QtButton(Gui.Widgets.Button, QtWidget):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__(window.findChild(QPushButton, name))

    def bindFunction(self, func: callable):
        self.origin.clicked.connect(func)

    def setText(self, text: str):
        self.origin.setText(text)
        

class QtTextbox(Gui.Widgets.Textbox, QtWidget):
    def __init__(self, origin):
        super().__init__(origin)

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


class QtLineEdit(QtTextbox):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__(window.findChild(QLineEdit, name))

    def setText(self, text: str):
        self.origin.setText(text)
        
    def setEditable(self, flag: bool):
        self.origin.setReadOnly(not flag)

        if flag is False:
            self.setColor(QColor(220, 220, 220))
        else:
            self.setColor(Qt.white)


class QtCombobox(QtTextbox):
    def __init__(self, window: QMainWindow, name: str):
        super().__init__(window.findChild(name))

    def setText(self, text: str):
        self.origin.setCurrentText(text)

    def setEditable(self, flag: bool):
        self.setEnabled(not flag)


if __name__ == "__main__":
    pass