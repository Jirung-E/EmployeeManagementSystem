from GuiController.GuiController import GuiController
from Gui.Windows import MainWindow
from GuiInterfaces.PyQt5.PyQt5Interface import *

from Main.MainWindow import EMS


def main():
    gui_interface: GuiInterface
    window: MainWindow
    
    gui_interface = PyQt5Interface()

    window = EMS()

    GuiController(gui_interface).run(window)


if __name__ == "__main__":
    main()