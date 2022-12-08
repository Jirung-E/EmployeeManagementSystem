from abc import ABC, abstractmethod
from typing import Dict

from Gui.Widgets import Textbox
from Gui.Widgets import Button


class Window(ABC):
    def __init__(self):
        self.textboxes: Dict[str, Textbox]
        self.buttons: Dict[str, Button]

    def _loadTextboxes(self):
        pass

    def _loadButtons(self):
        pass


class MainWindow(Window):
    def __init__(self, window):
        self.origin = window