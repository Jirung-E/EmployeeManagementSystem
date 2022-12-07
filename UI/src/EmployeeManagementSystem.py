from GuiController.GuiController import GuiController
from GuiInterfaces.PyQt5.PyQt5Interface import *

from GuiInterfaces.PyQt5.Windows.MainForm import MainWindow


def main():
    gui_interface: GuiInterface
    
    gui_interface = PyQt5Interface()
    GuiController(gui_interface).run(MainWindow())


if __name__ == "__main__":
    main()