from abc import ABC, abstractmethod
from typing import Dict

from Gui.Widgets import Textbox
from Gui.Widgets import Button


class Window(ABC):
    def __init__(self):
        self.textboxes: Dict[str, Textbox]
        self.buttons: Dict[str, Button]

        self.editable = False

    @abstractmethod
    def _loadTextboxes(self):
        pass

    @abstractmethod
    def _loadButtons(self):
        pass