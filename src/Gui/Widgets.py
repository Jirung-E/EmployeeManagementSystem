from abc import ABC, abstractmethod


class Widget(ABC):
    def __init__(self, origin=None):
        self.origin = origin

    @abstractmethod
    def setEnabled(self, flag: bool):
        pass

    @abstractmethod
    def setHidden(self, flag: bool):
        pass


class Button(Widget):
    def __init__(self, origin):
        super().__init__(origin)

    @abstractmethod
    def bindFunction(self, func: callable):
        pass

    @abstractmethod
    def setText(self, text: str):
        pass


class Textbox(Widget):
    def __init__(self, origin):
        super().__init__(origin)

    @abstractmethod
    def setEditable(self, flag: bool):
        pass

    @abstractmethod
    def setText(self, text: str):
        pass

    @abstractmethod
    def getCurrentText(self) -> str:
        pass

    def setColor(self, color):
        pass

    def setStyle(self, style_sheet: str):
        pass


class WidgetBox(Widget):
    def __init__(self, *widgets: Widget):
        self.widgets = widgets

    def __getitem__(self, index: int) -> Widget:
        return self.widgets[index]

    def setEnabled(self, flag: bool):
        for e in self.widgets:
            e.setEnabled(flag)

    def setHidden(self, flag: bool):
        for e in self.widgets:
            e.setHidden(flag)

    def setEditable(self, flag: bool):
        for e in self.widgets:
            if isinstance(e, Textbox):
                e.setEditable(flag)

    def setText(self, text: str):
        for e in self.widgets:
            if isinstance(e, Textbox):
                e.setText(text)