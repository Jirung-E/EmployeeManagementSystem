from abc import ABC, abstractmethod


class Widget(ABC):
    @abstractmethod
    def setEnabled(self, flag: bool):
        pass


class Button(Widget):
    def __init__(self):
        self.origin


class Textbox(Widget):
    def __init__(self):
        self.origin

    @abstractmethod
    def setEditable(self, flag: bool):
        pass

    @abstractmethod
    def setText(self, text: str):
        pass

    def setEnabled(self, flag: bool):
        pass

    def setColor(self, color):
        pass


class LineEdit(Textbox):
    def __init__(self, name: str):
        super().__init__()
        self.textboxes

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