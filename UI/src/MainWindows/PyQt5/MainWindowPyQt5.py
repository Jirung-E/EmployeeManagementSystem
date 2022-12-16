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

from MainWindows.PyQt5.LoadWindow import *
from MainWindows.PyQt5.PayWindow import *

from Data.Table import DataTable


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
            "about_workdate": QtButton(self.window.origin, "view_more_about_workdate_button")
        }

    def showData(self, data):
        self.window.textboxes["employee_number"].setText(data["사원번호"])
        self.window.textboxes["name"].setText(data["이름"])
        self.window.textboxes["address"].setText(data["주소"])
        self.window.textboxes["rrn"].setText(data["주민번호"])
        self.window.textboxes["phone_number"].setText(data["전화번호"])
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
        self.current_data: DataTable.Record = None
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

    def setEditable(self, flag: bool):
        self.is_editable = flag
        for e in self.textboxes.values():
            e.setEditable(flag)
        self.textboxes["pay"].setEditable(False)
        self.buttons["load"].setHidden(flag)
        self.buttons["add"].setHidden(flag)
        self.buttons["save_tool"].setHidden(flag)
        if flag is True:
            self.buttons["edit"].setText("취소")
            self.buttons["save"].setText("확인")
        else:
            self.buttons["edit"].setText("수정")
            self.buttons["save"].setText("저장(&S)")

    def popLoadWindow(self):
        sub = EMSLoadWindow()
        data, ok = sub.show()
        if ok:
            self.current_data = data
            if data == None:
                self.buttons["edit"].setEnabled(False)
                self.widgets.clear()
            else:
                self.buttons["edit"].setEnabled(True)
                self.widgets.showData(data)

    def clickEditButton(self):
        if self.is_editable:
            self.editCancel()
        else:
            self.editStart()
        
    def editStart(self):
        self.setEditable(True)

    def editCancel(self):
        self.setEditable(False)
        if self.current_data == None:
            self.buttons["edit"].setEnabled(False)
            self.widgets.clear()
        else:
            self.widgets.showData(self.current_data)

    def clickSaveButton(self):
        pass

    def clickSaveToolButton(self):
        pass

    def clickAddButton(self):
        self.widgets.clear()
        self.clickEditButton()
        self.buttons["edit"].setEnabled(True)

    def clickLoadButton(self):
        self.popLoadWindow()

    def clickViewMoreAboutPayButton(self):
        print("click view more about pay button")
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