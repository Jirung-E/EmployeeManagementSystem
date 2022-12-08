import tkinter

from GuiController.GuiInterface import GuiInterface


class TkinterInterface(GuiInterface):
    def __init__(self):
        pass

    def run(self, window):
        window.origin.mainloop()