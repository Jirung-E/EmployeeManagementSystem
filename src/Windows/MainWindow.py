from Gui.Windows import MainWindow
from Gui.Widgets import WidgetBox


# ----------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5 import uic

mainwindow = uic.loadUiType("./UI/mainwindow.ui")[0]

class MainForm(QMainWindow, mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# ----------------------------------------------------

from GuiInterfaces.PyQt5.Gui.Widgets import *

from Windows.LoadWindow import *
from Windows.PayWindow import *
from Windows.DutyChangeWindow import *
from Windows.WorkplaceChangeWindow import *
from Windows.LeaveWindow import *

from Data import *

import matplotlib.pyplot as mpl
import datetime

from pyqt_toast import Toast
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class EMSWidgetManager:
    def __init__(self, window: MainWindow):
        self.window = window

    def loadWidgets(self):
        self._loadTextboxes()
        self._loadButtons()

    def _loadTextboxes(self):
        self.window.textboxes = {
            "employee_number": QtLineEdit(self.window.origin, "employee_number_textbox"),
            "name": QtLineEdit(self.window.origin, "name_textbox"),
            "address": QtLineEdit(self.window.origin, "address_textbox"),
            "rrn": QtLineEdit(self.window.origin, "rrn_textbox"),
            "phone_number": QtLineEdit(self.window.origin, "phone_number_textbox"),
            "bank": WidgetBox(QtLineEdit(self.window.origin, "bank_textbox_1"), QtLineEdit(self.window.origin, "bank_textbox_2")),
            "duty": QtLineEdit(self.window.origin, "duty_textbox"),
            "pay": QtLineEdit(self.window.origin, "pay_textbox"),
            "workplace": QtLineEdit(self.window.origin, "workplace_textbox"),
            "start_date": QtLineEdit(self.window.origin, "startdate_textbox"),
            "end_date": QtLineEdit(self.window.origin, "enddate_textbox"),
        }

    def _loadButtons(self):
        self.window.buttons = {
            "load": QtButton(self.window.origin, "load_button"),
            "cancel": QtButton(self.window.origin, "cancel_button"), 
            "delete": QtButton(self.window.origin, "delete_button"), 
            "edit": QtButton(self.window.origin, "edit_button"), 
            "add": QtButton(self.window.origin, "add_button"),
            "ok": QtButton(self.window.origin, "ok_button"), 
            "save": QtButton(self.window.origin, "save_button"),
            "save_tool": QtButton(self.window.origin, "save_tool_button"),
            "about_pay": QtButton(self.window.origin, "view_more_about_pay_button"),
            "about_workdate": QtButton(self.window.origin, "view_more_about_workdate_button"),
            "duty_change": QtButton(self.window.origin, "duty_change_button"),
            "workplace_change": QtButton(self.window.origin, "workplace_change_button"),
            "leave": QtButton(self.window.origin, "leave_button"),
        }

    def showData(self, data):
        self.window.textboxes["employee_number"].setText(data["????????????"])
        self.window.textboxes["name"].setText(data["??????"])
        self.window.textboxes["address"].setText(data["??????"])
        self.window.textboxes["rrn"].setText(data["????????????"])
        self.window.textboxes["phone_number"].setText(data["????????????"])
        if data["??????"] != "":
            bank_account = data["??????"].split(' ')
            self.window.textboxes["bank"][0].setText(bank_account[0])
            self.window.textboxes["bank"][1].setText(bank_account[1])
        self.window.textboxes["duty"].setText(data["??????"])
        self.window.textboxes["pay"].setText(data["??????"])
        self.window.textboxes["workplace"].setText(data["?????????"])
        self.window.textboxes["start_date"].setText(data["?????????"])
        self.window.textboxes["end_date"].setText(data["?????????"])

    def clear(self):
        for e in self.window.textboxes.values():
            e.setText("")


class EMS(MainWindow):
    def __init__(self):
        super().__init__(MainForm())
        self.__widgets = EMSWidgetManager(self)
        self.__widgets.loadWidgets()
        self._bindFunctionsToButtons()
        self.__is_editable: bool = False
        self.adding: bool = False
        self.__data = Table("./testData/????????????.csv")
        self.__current_data: Table.Record = None
        self.__init()

    def _bindFunctionsToButtons(self):
        self.buttons["cancel"].bindFunction(self.clickCancelButton)
        self.buttons["delete"].bindFunction(self.clickDeleteButton)
        self.buttons["edit"].bindFunction(self.clickEditButton)
        self.buttons["ok"].bindFunction(self.clickOkButton)
        self.buttons["save"].bindFunction(self.clickSaveButton)
        self.buttons["save_tool"].bindFunction(self.clickSaveToolButton)
        self.buttons["add"].bindFunction(self.clickAddButton)
        self.buttons["load"].bindFunction(self.clickLoadButton)
        self.buttons["about_pay"].bindFunction(self.clickViewMoreAboutPayButton)
        self.buttons["about_workdate"].bindFunction(self.clickViewMoreAboutWorkdateButton)
        self.buttons["duty_change"].bindFunction(self.clickDutyChangeButton)
        self.buttons["workplace_change"].bindFunction(self.clickWorkplaceChangeButton)
        self.buttons["leave"].bindFunction(self.clickLeaveButton)

    def __init(self):
        self.setEditable(False)
        self.buttons["edit"].setEnabled(False)
        self.buttons["leave"].setHidden(True)

    def setEditable(self, flag: bool):
        self.__is_editable = flag
        self.setTextboxesEditable(flag)
        self.setButtonsEditable(flag)

    def setTextboxesEditable(self, flag: bool):
        for e in self.textboxes.values():
            e.setEditable(flag)
        self.textboxes["employee_number"].setEditable(False)
        self.textboxes["pay"].setEditable(False)
        self.textboxes["duty"].setEditable(False)
        self.textboxes["workplace"].setEditable(False)

    def setButtonsEditable(self, flag: bool):
        if self.__current_data == None:
            self.buttons["edit"].setEnabled(False)
        else:
            self.buttons["edit"].setEnabled(True)
        self.buttons["duty_change"].setEnabled(flag)
        self.buttons["workplace_change"].setEnabled(flag)
        self.buttons["add"].setHidden(flag)
        self.buttons["load"].setHidden(flag)
        self.buttons["save_tool"].setHidden(flag)
        self.buttons["edit"].setHidden(flag)
        self.buttons["add"].setHidden(flag)
        self.buttons["save"].setHidden(flag)
        self.buttons["cancel"].setHidden(not flag)
        self.buttons["delete"].setHidden(not flag)
        self.buttons["ok"].setHidden(not flag)

    def clickCancelButton(self):
        ok = self.yesOrNoWindow("??????", "????????? ????????? ???????????? ????????????.\n?????? ?????? ???????????????????")
        if ok:
            if self.adding:
                self.addCancel()
            else:
                self.editCancel()

    def clickDeleteButton(self):
        ok = self.yesOrNoWindow("??????", "?????? ?????? ???????????????????")
        if ok:
            self.deleteCurrentData()

    def deleteCurrentData(self):
        self.__data.delete(self.__current_data["????????????"])
        self.__current_data = None
        self.setEditable(False)
        self.buttons["edit"].setEnabled(False)
        self.buttons["leave"].setHidden(True)
        self.__widgets.clear()

    def clickEditButton(self):
        self.editStart()
        
    def editStart(self):
        self.setEditable(True)

    def editCancel(self):
        self.setEditable(False)
        if self.__current_data == None:
            self.buttons["edit"].setEnabled(False)
            self.__widgets.clear()
        else:
            self.__widgets.showData(self.__current_data)

    def editDone(self):
        self.setEditable(False)
        self.saveDatafromViewerToCurrentData()

    def saveDatafromViewerToCurrentData(self):
        self.__current_data["????????????"] = self.textboxes["employee_number"].getCurrentText()
        self.__current_data["??????"] = self.textboxes["name"].getCurrentText()
        self.__current_data["??????"] = self.textboxes["address"].getCurrentText()
        self.__current_data["????????????"] = self.textboxes["rrn"].getCurrentText()
        self.__current_data["????????????"] = self.textboxes["phone_number"].getCurrentText()
        self.__current_data["??????"] = self.textboxes["bank"][0].getCurrentText() + " " + self.textboxes["bank"][1].getCurrentText()
        self.__current_data["??????"] = self.textboxes["pay"].getCurrentText()
        self.__current_data["??????"] = self.textboxes["duty"].getCurrentText()
        self.__current_data["?????????"] = self.textboxes["workplace"].getCurrentText()
        self.__current_data["?????????"] = self.textboxes["start_date"].getCurrentText()
        self.__current_data["?????????"] = self.textboxes["end_date"].getCurrentText()

    def clickOkButton(self):
        if self.adding:
            self.addDone()
        else:
            self.editDone()

    def clickSaveButton(self):
        self.__data.save()
        toast = Toast("\n?????????????????????\n", parent=self.origin)
        toast.setOpacity(0.7)
        toast.setFont(QFont("Arial", 12, weight=80))
        toast.setAlignment(Qt.AlignCenter)
        toast.show()

    def clickSaveToolButton(self):
        print("click save tool button")

    def clickAddButton(self):
        self.addStart()

    def addStart(self):
        self.adding = True
        self.setEditable(True)
        self.__widgets.clear()
        self.buttons["delete"].setHidden(True)
        self.buttons["leave"].setHidden(True)
        today = datetime.datetime.now().date()
        self.textboxes["start_date"].setText(f"{today}")
        data = []
        for e in self.__data:
            if int(e["????????????"][0:4]) == today.year:
                data.append(int(e["????????????"][5:8]))
        if len(data) == 0:
            lastest = 0
        else:
            data = sorted(data, reverse=True)
            lastest = data[0]
        self.textboxes["employee_number"].setText(f"{today.year}-{lastest+1:0>3}")

    def addCancel(self):
        if self.__current_data == None:
            self.__widgets.clear()
        else:
            self.__widgets.showData(self.__current_data)
            self.buttons["leave"].setHidden(False)
        self.setEditable(False)

    def addDone(self):
        self.__current_data = self.__data.getNewEmptyRecord()
        self.saveDatafromViewerToCurrentData()
        self.buttons["leave"].setHidden(False)
        self.setEditable(False)

    def clickLoadButton(self):
        self.popLoadWindow()

    def popLoadWindow(self):
        sub = EMSLoadWindow(self.__data)
        data, ok = sub.show()
        if ok:
            self.__current_data = data
            self.buttons["edit"].setEnabled(True)
            self.buttons["leave"].setHidden(False)
            self.__widgets.showData(data)

    def clickViewMoreAboutPayButton(self):
        if self.__current_data == None:
            key = None
        else:
            key = self.__current_data["????????????"]
        sub = EMSPayWindow(key, self.__is_editable)
        total_pay, ok = sub.show()
        if ok and self.__is_editable:
            self.textboxes["pay"].setText(total_pay)

    def clickViewMoreAboutWorkdateButton(self):
        print("click view more about workdate button")

    def clickDutyChangeButton(self):
        sub = EMSDutyChangeWindow(self.textboxes["duty"].origin.text())
        duty, ok = sub.show()
        if ok:
            self.textboxes["duty"].setText(duty)

    def clickWorkplaceChangeButton(self):
        sub = EMSWorkplaceChangeWindow(self.textboxes["workplace"].origin.text())
        duty, ok = sub.show()
        if ok:
            self.textboxes["workplace"].setText(duty)

    def clickLeaveButton(self):
        if self.__current_data == None:
            key = None
        else:
            key = self.__current_data["????????????"]
        sub = EMSPayWindow(key, self.__is_editable)
        sub = EMSLeaveWindow(key, self.__is_editable)
        ok = sub.show()
        if ok:
            print("Hello")

    def yesOrNoWindow(self, title: str, description: str):
        sub = QDialog(self.origin)
        sub.setFixedSize(270, 120)
        sub.move(self.origin.x()+self.origin.width()//2-sub.width()//2, self.origin.y()+self.origin.height()//2-sub.height()//2)
        sub.setWindowTitle(title)
        sub.setFont(self.origin.font())
        main_layout = QVBoxLayout(sub)
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))
        cancel_button = QPushButton("?????????", sub)
        cancel_button.clicked.connect(sub.reject)
        button_layout.addWidget(cancel_button)
        ok_button = QPushButton("???", sub)
        ok_button.clicked.connect(sub.accept)
        button_layout.addWidget(ok_button)
        main_layout.addWidget(QLabel(description, sub))
        main_layout.addLayout(button_layout)
        sub.setLayout(main_layout)
        return sub.exec_()