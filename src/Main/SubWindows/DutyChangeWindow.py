from PyQt5.QtWidgets import *
from PyQt5 import uic

from GuiInterfaces.PyQt5.Gui.Widgets import *

from Data import List

duty_change_window = uic.loadUiType("./.ui/duty_change_window.ui")[0]

class EMSDutyChangeWindow(QDialog, duty_change_window):
    def __init__(self, current_duty: str = None):
        super().__init__()
        self.__current_data: str = current_duty
        self._initUI()
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        items = List("./data/직책.json").data()
        self.duty_select_textbox.addItems(items)
        if self.__current_data != None:
            self.duty_select_textbox.setCurrentText(self.__current_data)

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def show(self):
        ok = super().exec_()
        current_text = self.duty_select_textbox.currentText()
        return current_text, ok