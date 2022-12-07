from abc import ABC, abstractmethod


class GuiInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self, window):
        pass