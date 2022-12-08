from GuiController.GuiController import GuiController
from Gui.Windows import MainWindow
from GuiInterfaces.PyQt5.PyQt5Interface import *
from GuiInterfaces.Tkinter.TkinterInterface import *

from MainWindows.MainWindowPyQt5 import EMS
# from MainWindows.MainWindowTkinter import EMS


def main():
    gui_interface: GuiInterface
    window: MainWindow
    
    gui_interface = PyQt5Interface()
    # gui_interface = TkinterInterface()
    window = EMS()

    GuiController(gui_interface).run(window)


if __name__ == "__main__":
    main()