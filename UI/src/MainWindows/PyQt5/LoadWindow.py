from PyQt5.QtWidgets import *
from PyQt5 import uic

from Data.CSV import *

loadwindow = uic.loadUiType("./UI/loadwindow.ui")[0]

class EMSLoadWindow(QDialog, loadwindow):
    def __init__(self, data: CSVData):
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.ok_button.clicked.connect(self.ok)
        self.cancel_button.clicked.connect(self.cancel)
        # self.show()

    def ok(self):
        self.accept()

    def cancel(self):
        self.reject()

    def show(self):
        self.data.selectRow(0)
        header = f'[{self.data["사원번호"]}] {self.data["이름"]} ({self.data["사업장"]})'
        self.employee_list_textbox.addItem(header)
        for i in range(1, self.data.numOfRows()):
            self.data.selectRow(i)
            item = f'[{self.data["사원번호"]}] {self.data["이름"]} ({self.data["사업장"]})'
            if item == header:
                break
            self.employee_list_textbox.addItem(item)

        is_ok = super().exec_()

        return self.employee_list_textbox.currentIndex(), is_ok