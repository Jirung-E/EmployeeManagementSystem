from PyQt5.QtWidgets import *
from PyQt5 import uic

from GuiInterfaces.PyQt5.Gui.Widgets import *

from typing import Dict

from Data.Table import DataTable

pay_window = uic.loadUiType("./UI/pay_window.ui")[0]

class EMSPayWindow(QDialog, pay_window):
    def __init__(self, employee_number: str, is_editable: bool):
        super().__init__()
        self.__data = DataTable("./data/급여.csv").getRecordByKey(employee_number)
        self.__is_editable = is_editable
        self._initUI()
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        self.textboxes: Dict[str, QtTextbox] = {
            "default_pay": QtLineEdit(self, "default_pay_textbox"),
            "night_pay": QtLineEdit(self, "night_pay_textbox")
        }
        self.total = QtLineEdit(self, "total_pay_textbox")
        for e in self.textboxes.values():
            e.setEditable(self.__is_editable)
        self.total.setEditable(False)
        self.textboxes["default_pay"].origin.textChanged.connect(self.__calcTotalPay)
        self.textboxes["night_pay"].origin.textChanged.connect(self.__calcTotalPay)
        if self.__data != None:
            self.textboxes["default_pay"].setText(self.__data["기본"])
            self.textboxes["night_pay"].setText(self.__data["야간"])

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def show(self):
        ok = super().exec_()
        total_pay = self.total.origin.text()
        return total_pay, ok

    def __calcTotalPay(self):
        result = 0
        for e in self.textboxes.values():
            if e.origin.text() == "":
                continue
            result += int(e.origin.text())
        self.total.setText(str(result))