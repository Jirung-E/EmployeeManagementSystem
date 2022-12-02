import sys

from PyQt5.QtWidgets import *

from Ui import MainWindow


def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    run()