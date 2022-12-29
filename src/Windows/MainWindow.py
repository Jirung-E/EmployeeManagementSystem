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
            "edit": QtButton(self.window.origin, "edit_button"), 
            "save": QtButton(self.window.origin, "save_button"),
            "save_tool": QtButton(self.window.origin, "save_tool_button"),
            "add": QtButton(self.window.origin, "add_button"),
            "load": QtButton(self.window.origin, "load_button"),
            "about_pay": QtButton(self.window.origin, "view_more_about_pay_button"),
            "about_workdate": QtButton(self.window.origin, "view_more_about_workdate_button"),
            "duty_change": QtButton(self.window.origin, "duty_change_button"),
            "workplace_change": QtButton(self.window.origin, "workplace_change_button"),
        }

    def showData(self, data):
        self.window.textboxes["employee_number"].setText(data["사원번호"])
        self.window.textboxes["name"].setText(data["이름"])
        self.window.textboxes["address"].setText(data["주소"])
        self.window.textboxes["rrn"].setText(data["주민번호"])
        self.window.textboxes["phone_number"].setText(data["전화번호"])
        if data["계좌"] != "":
            bank_account = data["계좌"].split(' ')
            self.window.textboxes["bank"][0].setText(bank_account[0])
            self.window.textboxes["bank"][1].setText(bank_account[1])
        self.window.textboxes["duty"].setText(data["직책"])
        self.window.textboxes["pay"].setText(data["급여"])
        self.window.textboxes["workplace"].setText(data["근무지"])
        self.window.textboxes["start_date"].setText(data["입사일"])
        self.window.textboxes["end_date"].setText(data["퇴사일"])

    def clear(self):
        for e in self.window.textboxes.values():
            e.setText("")


class EMS(MainWindow):
    def __init__(self):
        super().__init__(MainForm())
        self.widgets = EMSWidgetManager(self)
        self.widgets.loadWidgets()
        self._bindFunctionsToButtons()
        self.is_editable: bool = False
        self.data = Table("./testData/직원정보.csv")
        self.current_data: Table.Record = None
        self.setEditable(False)
        self.buttons["edit"].setEnabled(False)

    def _bindFunctionsToButtons(self):
        self.buttons["edit"].bindFunction(self.clickEditButton)
        self.buttons["save"].bindFunction(self.clickSaveButton)
        self.buttons["save_tool"].bindFunction(self.clickSaveToolButton)
        self.buttons["add"].bindFunction(self.clickAddButton)
        self.buttons["load"].bindFunction(self.clickLoadButton)
        self.buttons["about_pay"].bindFunction(self.clickViewMoreAboutPayButton)
        self.buttons["about_workdate"].bindFunction(self.clickViewMoreAboutWorkdateButton)
        self.buttons["duty_change"].bindFunction(self.clickDutyChangeButton)
        self.buttons["workplace_change"].bindFunction(self.clickWorkplaceChangeButton)

    def setEditable(self, flag: bool):
        self.is_editable = flag
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
        self.buttons["duty_change"].setEnabled(flag)
        self.buttons["workplace_change"].setEnabled(flag)
        self.buttons["add"].setHidden(flag)
        self.buttons["load"].setHidden(flag)
        self.buttons["save_tool"].setHidden(flag)
        if flag is True:
            self.buttons["edit"].setText("취소")
            self.buttons["add"].setText("삭제")
            self.buttons["add"].origin.setStyleSheet('Color : red')
            self.buttons["save"].setText("확인")
        else:
            self.buttons["edit"].setText("수정")
            self.buttons["add"].setText("추가")
            self.buttons["add"].origin.setStyleSheet('Color : black')
            self.buttons["save"].setText("저장(&S)")

    def clickEditButton(self):
        if self.is_editable:
            sub = QDialog(self.origin)
            sub.setFixedSize(270, 120)
            sub.move(self.origin.x()+self.origin.width()//2-sub.width()//2, self.origin.y()+self.origin.height()//2-sub.height()//2)
            sub.setWindowTitle("취소")
            sub.setFont(self.origin.font())
            main_layout = QVBoxLayout(sub)
            button_layout = QHBoxLayout()
            button_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))
            cancel_button = QPushButton("아니오", sub)
            cancel_button.clicked.connect(sub.reject)
            button_layout.addWidget(cancel_button)
            ok_button = QPushButton("예", sub)
            ok_button.clicked.connect(sub.accept)
            button_layout.addWidget(ok_button)
            main_layout.addWidget(QLabel("편집한 내용이 저장되지 않습니다.\n정말 취소 하시겠습니까?", sub))
            main_layout.addLayout(button_layout)
            sub.setLayout(main_layout)
            ok = sub.exec_()
            if ok:
                self.editCancel()
        else:
            self.editStart()
        
    def editStart(self):
        self.setEditable(True)
        self.buttons["add"].setHidden(False)

    def editCancel(self):
        self.setEditable(False)
        if self.current_data == None:
            self.buttons["edit"].setEnabled(False)
            self.widgets.clear()
        else:
            self.widgets.showData(self.current_data)

    def editDone(self):
        self.setEditable(False)
        if self.current_data != None:
            if self.current_data["사원번호"] != self.textboxes["employee_number"].getCurrentText():
                self.current_data = self.data.getNewEmptyRecord()
        else:
            self.current_data = self.data.getNewEmptyRecord()
        self.current_data["사원번호"] = self.textboxes["employee_number"].getCurrentText()
        self.current_data["이름"] = self.textboxes["name"].getCurrentText()
        self.current_data["주소"] = self.textboxes["address"].getCurrentText()
        self.current_data["주민번호"] = self.textboxes["rrn"].getCurrentText()
        self.current_data["전화번호"] = self.textboxes["phone_number"].getCurrentText()
        self.current_data["계좌"] = self.textboxes["bank"][0].getCurrentText() + " " + self.textboxes["bank"][1].getCurrentText()
        self.current_data["급여"] = self.textboxes["pay"].getCurrentText()
        self.current_data["직책"] = self.textboxes["duty"].getCurrentText()
        self.current_data["근무지"] = self.textboxes["workplace"].getCurrentText()
        self.current_data["입사일"] = self.textboxes["start_date"].getCurrentText()
        self.current_data["퇴사일"] = self.textboxes["end_date"].getCurrentText()

    def clickSaveButton(self):
        if self.is_editable:
            self.editDone()
        else:
            self.data.save()
            toast = Toast("\n저장되었습니다\n", parent=self.origin)
            toast.setOpacity(0.7)
            toast.setFont(QFont("Arial", 12, weight=80))
            toast.setAlignment(Qt.AlignCenter)
            toast.show()

    def clickSaveToolButton(self):
        print("click save tool button")

    def clickAddButton(self):
        if self.is_editable:
            sub = QDialog(self.origin)
            sub.setFixedSize(270, 120)
            sub.move(self.origin.x()+self.origin.width()//2-sub.width()//2, self.origin.y()+self.origin.height()//2-sub.height()//2)
            sub.setWindowTitle("삭제")
            sub.setFont(self.origin.font())
            main_layout = QVBoxLayout(sub)
            button_layout = QHBoxLayout()
            button_layout.addItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Minimum))
            cancel_button = QPushButton("아니오", sub)
            cancel_button.clicked.connect(sub.reject)
            button_layout.addWidget(cancel_button)
            ok_button = QPushButton("예", sub)
            ok_button.clicked.connect(sub.accept)
            button_layout.addWidget(ok_button)
            main_layout.addWidget(QLabel("현재 데이터가 영구적으로 소실됩니다.\n정말 삭제 하시겠습니까?", sub))
            main_layout.addLayout(button_layout)
            sub.setLayout(main_layout)
            ok = sub.exec_()
            if ok:
                self.deleteCurrentData()
                return
        self.widgets.clear()
        self.setEditable(True)
        self.buttons["edit"].setEnabled(True)
        today = datetime.datetime.now().date()
        self.textboxes["start_date"].setText(f"{today}")
        data = []
        for e in self.data:
            if int(e["사원번호"][0:4]) == today.year:
                data.append(int(e["사원번호"][5:8]))
        if len(data) == 0:
            lastest = 0
        else:
            data = sorted(data, reverse=True)
            lastest = data[0]
        self.textboxes["employee_number"].setText(f"{today.year}-{lastest+1:0>3}")

    def deleteCurrentData(self):
        self.data.delete(self.current_data["사원번호"])
        self.current_data = None
        self.setEditable(False)
        self.buttons["edit"].setEnabled(False)
        self.widgets.clear()

    def clickLoadButton(self):
        self.popLoadWindow()

    def popLoadWindow(self):
        sub = EMSLoadWindow(self.data)
        data, ok = sub.show()
        if ok:
            self.current_data = data
            if data == None:
                self.buttons["edit"].setEnabled(False)
                self.widgets.clear()
            else:
                self.buttons["edit"].setEnabled(True)
                self.widgets.showData(data)

    def clickViewMoreAboutPayButton(self):
        if self.current_data == None:
            key = None
        else:
            key = self.current_data["사원번호"]
        sub = EMSPayWindow(key, self.is_editable)
        total_pay, ok = sub.show()
        if ok and self.is_editable:
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