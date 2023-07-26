from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from GuiInterfaces.PyQt5.Gui.Widgets import *

from Data import List


class ListViewWindow(QDialog, uic.loadUiType("./.ui/list_view_window.ui")[0]):
    def __init__(self, data: List, title: str, label: str):
        super().__init__()
        self.__data: List = data
        self.__filtered_data_index: list = []
        self._initUI()
        self.setWindowTitle(title)
        self.label.setText(label)
        self._bindFunctionsToButtons()
        self.search_textbox.textChanged.connect(self.__textboxUpdated)
        self.list_view.doubleClicked.connect(self.accept)
        self.list_view.clicked.connect(self.__listViewUpdated)

    def __del__(self):
        self.__data.save()

    def _initUI(self):
        self.setupUi(self)
        self.add_button.setEnabled(False)
        self.ok_button.setEnabled(False)
        model = QStandardItemModel()
        for e in self.__data:
            model.appendRow(QStandardItem(e))
        self.list_view.setModel(model)

    def _bindFunctionsToButtons(self):
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.search_button.clicked.connect(self.__search)
        self.add_button.clicked.connect(self.__add)

    def show(self):
        ok = super().exec_()
        current_text = ""
        index = self.list_view.currentIndex()
        if index.row() != -1:
            current_text = self.list_view.model().itemFromIndex(index).text()
        return current_text, ok

    def __search(self):
        text = self.search_textbox.text().replace(' ', '').lower()
        if text == "":
            # 전체 리스트를 출력하도록 모델 업데이트
            self.__filtered_data_index = []
            model = QStandardItemModel()
            for e in self.__data:
                model.appendRow(QStandardItem(e))
            self.list_view.setModel(model)

            self.add_button.setEnabled(False)

            return
        
        # 필터링된 리스트만 출력하도록 모델 업데이트
        self.add_button.setEnabled(True)
        
        self.__filtered_data_index = []
        for i in range(0, self.__data.data().__len__()):
            if self.__data[i].replace(' ', '').lower().find(text) != -1:
                if self.__data[i] == text:
                    self.add_button.setEnabled(False)
                self.__filtered_data_index.append(i)

        model = QStandardItemModel()
        for e in [ self.__data[i] for i in self.__filtered_data_index ]:
            model.appendRow(QStandardItem(e))
        self.list_view.setModel(model)
        
    def __add(self):
        self.__data.add(self.search_textbox.text())
        self.add_button.setEnabled(False)
        self.__search()

    def __textboxUpdated(self):
        self.add_button.setEnabled(False)

    def __listViewUpdated(self):
        if len(self.list_view.selectedIndexes()) == 0:
            self.ok_button.setEnabled(False)
        else:
            self.ok_button.setEnabled(True)