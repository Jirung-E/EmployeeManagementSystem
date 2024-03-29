from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from datetime import date

from Main.SubWindows.YesOrNoWindow import *

from Data import Table

leave_window = uic.loadUiType("./.ui/leave_window.ui")[0]

class EMSLeaveWindow(QDialog, leave_window):
    def __init__(self, data: Table, employee_number: str, is_editable: bool):
        super().__init__()
        self.__data = data
        self.__current_data = data.getRecordByKey(employee_number)
        self.employee_number = employee_number
        self._initUI()
        self.__showList()
        self.__setEditable(is_editable)
        self._bindFunctionsToButtons()

    def _initUI(self):
        self.setupUi(self)
        self.start_date.dateChanged.connect(self.startDateChanged)
        self.end_date.dateChanged.connect(self.endDateChanged)
        self.half_checkbox.clicked.connect(self.halfCheckboxUpdated)
        self.start_date.setDate(date.today())
        self.end_date.setDate(self.start_date.date())
        self.delete_button.setEnabled(False)

    def _bindFunctionsToButtons(self):
        self.close_button.clicked.connect(self.close)
        self.show_on_calendar_1.clicked.connect(self.showCalendar1)
        self.show_on_calendar_2.clicked.connect(self.showCalendar2)
        self.add_button.clicked.connect(self.clickAddButton)
        self.delete_button.clicked.connect(self.clickDeleteButton)
        self.list_view.clicked.connect(self.__listViewUpdated)

    def show(self):
        super().exec_()

    def __showList(self):
        if self.__current_data == None:
            return
        model = QStandardItemModel()
        if self.__current_data["내역"] == "":
            self.list_view.setModel(model)
            return
        self.leave_list: list = self.__current_data["내역"].split(',')
        leave_list = self.leave_list[::-1]
        for e in leave_list:
            leave = e.split(':')
            days = leave[1].split("~")
            item = f'{days[0]} ~ {days[1]}  ({leave[0]}일)'
            model.appendRow(QStandardItem(item))
        self.list_view.setModel(model)

    def __setEditable(self, flag: bool):
        self.start_date.setEnabled(flag)
        self.end_date.setEnabled(flag)
        self.show_on_calendar_1.setEnabled(flag)
        self.show_on_calendar_2.setEnabled(flag)
        self.half_checkbox.setEnabled(flag)
        self.add_button.setEnabled(flag)
        # self.delete_button.setEnabled(flag)
        self.list_view.setEnabled(flag)

    def __listViewUpdated(self):
        if len(self.list_view.selectedIndexes()) == 0:
            self.delete_button.setEnabled(False)
        else:
            self.delete_button.setEnabled(True)

    def startDateChanged(self):
        if self.half_checkbox.isChecked():
            self.end_date.setDate(self.start_date.date())
            return
        if self.start_date.date() > self.end_date.date():
            self.end_date.setDate(self.start_date.date())
        self.updateTotal()

    def endDateChanged(self):
        if self.half_checkbox.isChecked():
            return
        if self.end_date.date() < self.start_date.date():
            self.start_date.setDate(self.end_date.date())
        self.updateTotal()

    def updateTotal(self):
        sd = date(self.start_date.date().year(), self.start_date.date().month(), self.start_date.date().day())
        ed = date(self.end_date.date().year(), self.end_date.date().month(), self.end_date.date().day())
        self.total.setText(f"{(ed-sd).days+1}")

    def showCalendar(self, target_datebox: QDateEdit):
        cal = QDialog(self)
        cal.setWindowTitle("달력")
        main_layout = QVBoxLayout()
        calendar = QCalendarWidget()
        calendar.setSelectedDate(target_datebox.date())
        main_layout.addWidget(calendar)
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))
        cancel_button = QPushButton("아니오", cal)
        cancel_button.clicked.connect(cal.reject)
        button_layout.addWidget(cancel_button)
        ok_button = QPushButton("예", cal)
        ok_button.clicked.connect(cal.accept)
        button_layout.addWidget(ok_button)
        main_layout.addLayout(button_layout)
        cal.setLayout(main_layout)
        ok = cal.exec_()
        if ok:
            target_datebox.setDate(calendar.selectedDate())

    def showCalendar1(self):
        self.showCalendar(self.start_date)

    def showCalendar2(self):
        self.showCalendar(self.end_date)

    def halfCheckboxUpdated(self):
        if self.half_checkbox.isChecked():
            self.end_date.setEnabled(False)
            self.show_on_calendar_2.setEnabled(False)
            self.end_date.setDate(self.start_date.date())
            self.total.setText(f"0.5")
        else:
            self.end_date.setEnabled(True)
            self.show_on_calendar_2.setEnabled(True)
            self.updateTotal()

    def clickAddButton(self):
        ok = YesOrNoWindow("추가", "정말 추가 하시겠습니까?", self).show()
        if ok:
            self.add()
            self.__showList()
            self.delete_button.setEnabled(False)

    def clickDeleteButton(self):
        if self.list_view.currentIndex().row() == -1:
            return
        ok = YesOrNoWindow("삭제", "정말 삭제 하시겠습니까?", self).show()
        if ok:
            self.delete()
            self.__showList()
            self.delete_button.setEnabled(False)

    def delete(self):
        for i in self.list_view.selectedIndexes():
            print(i.row())
            self.leave_list[len(self.leave_list)-1 - i.row()] = ""
            print("ok")
        for i in range(len(self.leave_list), 0, -1):
            if self.leave_list[i-1] == "":
                self.leave_list.pop(i-1)
        self.__current_data["내역"] = ",".join(self.leave_list)

    def add(self):
        if self.__current_data == None:
            self.__current_data = self.__data.getNewEmptyRecord()
            self.__current_data["사원번호"] = self.employee_number
        total = self.total.text()
        leave = total + ":" + self.start_date.text() + "~" + self.end_date.text()
        if self.__current_data["내역"] == "":
            self.__current_data["내역"] = leave
        else:
            self.__current_data["내역"] += "," + leave