from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIntValidator

from GuiInterfaces.PyQt5.Gui.Widgets import *

from typing import Dict

from Data.Table import Table

pay_window = uic.loadUiType("./UI/pay_window.ui")[0]

class EMSPayWindow(QDialog, pay_window):
    __data = Table("./data/급여.csv")

    def __init__(self, employee_number: str, is_editable: bool):
        super().__init__()
        self.__current_data = EMSPayWindow.__data.getRecordByKey(employee_number)
        self.__is_editable = is_editable
        self._initUI()
        self.__showCurrentData()
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        self.total = QtLineEdit(self, "total_pay_textbox")
        self.total.setEditable(False)

        main_layout = self.contents_layout
        attr = EMSPayWindow.__data.getAttributes()[1:]
        self.textboxes: Dict[str, QtTextbox] = { name: QtLineEdit(self, name) for name in attr }
        form = QFormLayout()
        form.setSpacing(10)
        val = QIntValidator()
        for e in self.textboxes.items():
            e[1].setEditable(self.__is_editable)
            e[1].origin.textChanged.connect(self.__calcTotalPay)
            e[1].origin.setValidator(val)
            form.addRow(e[0], e[1].origin)
        main_layout.addLayout(form)

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def accept(self):
        super().accept()
        if self.__current_data == None:
            return
        for e in self.textboxes.items():
            self.__current_data[e[0]] = e[1].getCurrentText()
        self.__data.save()

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

    def __showCurrentData(self):
        if self.__current_data == None:
            return
        for e in self.textboxes.items():
            e[1].setText(self.__current_data[e[0]])