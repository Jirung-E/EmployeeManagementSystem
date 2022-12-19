from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from Data.Table import Table
import json

from typing import List

loadwindow = uic.loadUiType("./UI/load_window.ui")[0]

class ListViewer:
    def __init__(self, origin: QListView):
        self.__origin = origin

    def show(self, data: List[Table.Record]):
        model = QStandardItemModel()
        for e in data:
            item = f'[{e["사원번호"]}] {e["이름"]} ({e["근무지"]} {e["직책"]})'
            model.appendRow(QStandardItem(item))
        self.__origin.setModel(model)

class EMSLoadWindow(QDialog, loadwindow):
    def __init__(self, data: Table):
        super().__init__()
        self.__data = data
        self._initUI()
        self._bindFunctionsToButtons()
        self.__viewer = ListViewer(self.list_view)
        self.__updateViewer()

    def _initUI(self):
        self.setupUi(self)
        self.__setUpFilters()
        self.__setUpOrderByList()
        self.__setUpEmployeeList()

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.search_button.clicked.connect(self.__showSearchResult)
        self.sort_rule_button.clicked.connect(self.__changeSortRule)

    def show(self):
        ok = super().exec_()
        data = None
        if ok:
            index = self.list_view.currentIndex()
            if index.row() != -1:
                key = self.list_view.model().itemFromIndex(index).text()[1:9]
                data = self.__data.getRecordByKey(key)
        return data, ok

    def __setUpEmployeeList(self):
        self.__employee_list: List[Table.Record] = []
        for e in self.__data:
            self.__employee_list.append(e)

    def __setUpFilters(self):
        self.search_filter_1.activated.connect(self.__updateFilter1)
        self.search_filter_2.activated.connect(self.__showFilteredResult)
        self.search_filter_2.setEnabled(False)
        self.__setUpFilter1()

    def __setUpFilter1(self):
        self.search_filter_1.addItem("전체")
        self.search_filter_1.addItem("사업장")
        self.search_filter_1.addItem("직책")

    def __updateFilter1(self):
        current_filter = self.search_filter_1.currentText()
        self.search_textbox.clear()
        if current_filter == "전체":
            self.__setUpEmployeeList()
            self.__updateViewer()
            self.search_filter_2.setEnabled(False)
            return
        self.__setFilter2(current_filter)
        self.__showFilteredResult()

    def __setFilter2(self, filter: str):
        self.search_filter_2.clear()
        self.search_filter_2.setEnabled(True)
        f = open("./data/" + filter + ".json", encoding="utf-8")
        items = json.load(f)
        self.search_filter_2.addItems(items)

    def __showFilteredResult(self):
        self.search_textbox.clear()
        current_text = self.search_filter_2.currentText()
        attribute = self.search_filter_1.currentText()
        if attribute == "사업장":
            attribute = "근무지"
        self.__employee_list.clear()
        for e in self.__data:
            if e[attribute] == current_text:
                self.__employee_list.append(e)
        self.__updateViewer()

    def __showSearchResult(self):
        text = self.search_textbox.text()
        if text == "":
            self.__setUpEmployeeList()
            return
        employee_list = list(self.__employee_list)
        self.__employee_list = []
        for e in employee_list:
            for d in e.data():
                if d.find(text) != -1:
                    self.__employee_list.append(e)
                    break
        self.__updateViewer()
        self.__employee_list = employee_list

    def __setUpOrderByList(self):
        self.order_by_textbox.addItems(["사원번호", "이름", "입사일", "퇴사일"])
        self.order_by_textbox.activated.connect(self.__updateOrderByTextbox)
        self.__sort_ascending = True

    def __updateOrderByTextbox(self):
        self.__updateViewer()

    def __changeSortRule(self):
        self.__sort_ascending = not self.__sort_ascending
        if self.__sort_ascending:
            self.sort_rule_button.setText("오름차순")
        else:
            self.sort_rule_button.setText("내림차순")
        self.__updateViewer()

    def __sort(self):
        self.__orderBy(self.order_by_textbox.currentText())

    def __orderBy(self, key: str):
        self.__employee_list = sorted(self.__employee_list, key=lambda x: x[key], reverse=not self.__sort_ascending)

    def __updateViewer(self):
        self.__sort()
        self.__viewer.show(self.__employee_list)

    def __getListToBeShown(self):
        if self.__triggered(self.search_filter_2):
            return self.__getFilteredList()
        elif self.__triggered(self.search_button):
            return self.__getSearchResultList()