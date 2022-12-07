from GuiController.GuiInterface import GuiInterface


class GuiController:
    def __init__(self, gui_interface: GuiInterface):
        self.gui = gui_interface

    def run(self, window):
        self.gui.run(window)