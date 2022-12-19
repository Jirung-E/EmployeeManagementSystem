from GuiController.GuiInterface import GuiInterface
from Gui.Windows import Window


class GuiController:
    def __init__(self, gui_interface: GuiInterface):
        self.gui = gui_interface

    def run(self, window: Window):
        self.gui.run(window)