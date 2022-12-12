from PyQt5.QtWidgets import *
from PyQt5 import uic

from Data.CSV import *

from MainWindows.PyQt5.SearchWindow import SearchWindow

loadwindow = uic.loadUiType("./UI/loadwindow.ui")[0]

class EMSLoadWindow(QDialog, loadwindow):
    current_index = 0

    def __init__(self, data: CSVData):
        super().__init__()
        self.data = data
        self._initUI()
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        self.__setFilter()
        self.__setEmployeeList()

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.search_button.clicked.connect(self.__popSearchWindow)

    def show(self):
        is_ok = super().exec_()
        if is_ok:
            EMSLoadWindow.current_index = self.employee_list_textbox.currentIndex()
        return EMSLoadWindow.current_index, is_ok

    def __popSearchWindow(self):
        index, ok = SearchWindow(self.data).show()
        if ok:
            EMSLoadWindow.current_index = index
            self.__update()

    def __setEmployeeList(self):
        for i in range(0, self.data.numOfRows()):
            self.data.selectRow(i)
            item = f'[{self.data["사원번호"]}] {self.data["이름"]} ({self.data["사업장"]})'
            self.employee_list_textbox.addItem(item)
        self.data.selectRow(0)
        self.__update()

    def __setFilter(self):
        self.search_filter_1.activated.connect(self.__setFilter2)
        self.search_filter_2.setEnabled(False)
        self.search_filter_1.addItem("전체")
        self.search_filter_1.addItem("근무지")
        self.search_filter_1.addItem("직책")

    def __setFilter2(self):
        self.search_filter_2.activated.connect(self.__showFilteredResult)
        self.search_filter_2.clear()
        current_text = self.search_filter_1.currentText()
        if current_text == "전체":
            self.search_filter_2.setEnabled(False)
        else:
            self.search_filter_2.setEnabled(True)
            if current_text == "근무지":
                self.search_filter_2.addItem("PY TOWER")
                self.search_filter_2.addItem("CS 상가")
            elif current_text == "직책":
                self.search_filter_2.addItem("경비원")
                self.search_filter_2.addItem("미화원")

    def __showFilteredResult(self):
        pass

    def __update(self):
        self.employee_list_textbox.setCurrentIndex(EMSLoadWindow.current_index)