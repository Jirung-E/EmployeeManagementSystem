from abc import ABC, abstractmethod
from typing import Dict


class Widget(ABC):
    def setEnabled(self, flag: bool):
        pass


class Button(Widget):
    def __init__(self, origin):
        self.origin = origin

    @abstractmethod
    def bindFunction(self, func: callable):
        pass

    def setText(self, text: str):
        pass


class Textbox(Widget):
    def __init__(self):
        self.origin = None

    @abstractmethod
    def setEditable(self, flag: bool):
        pass

    @abstractmethod
    def setText(self, text: str):
        pass

    def setColor(self, color):
        pass


class LineEdit(Textbox):
    def __init__(self, name: str):
        super().__init__()

    def setText(self, text: str):
        pass
        
    def setEditable(self, flag: bool):
        pass


class Combobox(Textbox):
    def __init__(self, name: str):
        pass

    def setText(self, text: str):
        pass

    def setEditable(self, flag: bool):
        pass


class WidgetBox(Widget):
    def __init__(self, *widgets: Widget):
        self.widgets = widgets

    def __getitem__(self, index: int) -> Widget:
        return self.widgets[index]

    def setEnabled(self, flag: bool):
        for e in self.widgets:
            e.setEnabled(flag)

    def setEditable(self, flag: bool):
        for e in self.widgets:
            if isinstance(e, Textbox):
                e.setEditable(flag)