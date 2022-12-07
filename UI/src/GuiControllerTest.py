from GuiController.GuiController import GuiController
from GuiInterfaces.PyQt5.PyQt5Interface import *
from GuiInterfaces.Tkinter.TkinterInterface import *


def test():
    interface: GuiInterface
    controller: GuiController
    window = None

    interface = PyQt5Interface()
    controller = GuiController(interface)
    window = QMainWindow()

    controller.run(window)

    interface = TkinterInterface()
    controller = GuiController(interface)
    window = tkinter.Tk()

    controller.run(window)


if __name__ == "__main__":
    test()