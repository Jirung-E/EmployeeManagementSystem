from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from Data.CSV import *

searchwindow = uic.loadUiType("./UI/searchwindow.ui")[0]

class SearchWindow(QDialog, searchwindow):
    def __init__(self, data: CSVData):
        super().__init__()
        self._initUI()
        self._bindFunctionsToButtons()
        self.data = data
        self.employee_list_model = QStandardItemModel()
        for i in range(1, self.data.numOfRows()):
            self.data.selectRow(i)
            self.employee_list_model.appendRow(QStandardItem(self.data["이름"]))
        self.list_view.setModel(self.employee_list_model)

    def _initUI(self):
        self.setupUi(self)

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def show(self):
        is_ok = super().exec_()
        value = self.list_view.currentIndex().row() + 1
        return value, is_ok