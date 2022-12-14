from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from Data.Table import DataTable
import json

loadwindow = uic.loadUiType("./UI/load_window.ui")[0]

class EMSLoadWindow(QDialog, loadwindow):
    def __init__(self):
        super().__init__()
        self.data = DataTable("./data/data.csv")
        self._initUI()
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        self.__setUpEmployeeList()
        self.__setUpFilters()

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.search_button.clicked.connect(self.__showSearchResult)

    def show(self):
        ok = super().exec_()
        data = None
        if ok:
            index = self.list_view.currentIndex()
            print(index)
            key = self.list_view.model().itemFromIndex(index).text()[1:9]
            print(key)
            for i in range(0, self.data.getNumOfRecords()):
                if self.data[i]["사원번호"] == key:
                    data = self.data[i]
                    break
        return data, ok

    def __setUpEmployeeList(self):
        employee_list_model = QStandardItemModel()
        for i in range(0, self.data.getNumOfRecords()):
            data = self.data[i]
            item = f'[{data["사원번호"]}] {data["이름"]} ({data["근무지"]})'
            employee_list_model.appendRow(QStandardItem(item))
        self.list_view.setModel(employee_list_model)

    def __setUpFilters(self):
        self.search_filter_1.activated.connect(self.__setFilter2)
        self.search_filter_2.activated.connect(self.__showFilteredResult)
        self.search_filter_2.setEnabled(False)
        self.__setUpFilter1()

    def __setUpFilter1(self):
        self.search_filter_1.addItem("전체")
        self.search_filter_1.addItem("사업장")
        self.search_filter_1.addItem("직책")

    def __setFilter2(self):
        self.search_filter_2.clear()
        current_text = self.search_filter_1.currentText()
        if current_text == "전체":
            self.search_filter_2.setEnabled(False)
            return
        self.search_filter_2.setEnabled(True)
        f = open("./data/" + current_text + ".json", encoding="utf-8")
        items = json.load(f)
        self.search_filter_2.addItems(items)

    def __showFilteredResult(self):
        employee_list_model = QStandardItemModel()
        current_text = self.search_filter_2.currentText()
        attribute = self.search_filter_1.currentText()
        if attribute == "사업장":
            attribute = "근무지"
        for i in range(0, self.data.getNumOfRecords()):
            data = self.data[i]
            if current_text == data[attribute]:
                item = f'[{data["사원번호"]}] {data["이름"]} ({data["근무지"]})'
                employee_list_model.appendRow(QStandardItem(item))
        self.list_view.setModel(employee_list_model)

    def __showSearchResult(self):
        text = self.search_textbox.text()
        if text == "":
            return
        employee_list_model = QStandardItemModel()
        for i in range(0, self.data.getNumOfRecords()):
            data = self.data[i]
            for e in data.data():
                if e.find(text) != -1:
                    item = f'[{data["사원번호"]}] {data["이름"]} ({data["근무지"]}) \t\t\t - ({e})'
                    employee_list_model.appendRow(QStandardItem(item))
                    break
        self.list_view.setModel(employee_list_model)