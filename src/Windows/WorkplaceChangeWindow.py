from PyQt5.QtWidgets import *
from PyQt5 import uic

from GuiInterfaces.PyQt5.Gui.Widgets import *

from Data import List

workplace_change_window = uic.loadUiType("./UI/duty_change_window.ui")[0]

class EMSWorkplaceChangeWindow(QDialog, workplace_change_window):
    def __init__(self, current_data: str = None):
        super().__init__()
        self.__current_data: str = current_data
        self._initUI()
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        items = List("./data/사업장.json").data()
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