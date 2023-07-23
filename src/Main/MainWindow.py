from Gui.Windows import MainWindow
from Gui.Widgets import WidgetBox
from GuiInterfaces.PyQt5.Gui.Widgets import *
from Main.SubWindows import *
from Main.DataManager import *
from Data import *

from datetime import datetime

from pyqt_toast import Toast
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


# ----------------------------------------------------
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCloseEvent
from PyQt5 import uic

mainwindow = uic.loadUiType("./.ui/mainwindow.ui")[0]

class MainForm(QMainWindow, mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_saved = True
        
    def closeEvent(self, event: QCloseEvent):
        if self.is_saved:
            event.accept()
            return
        ok = YesOrNoWindow("종료", "편집한 내용이 저장되지 않았습니다.\n저장하지않고 종료 하시겠습니까?", self).show()
        if ok:
            event.accept()
        else:
            event.ignore()

# ----------------------------------------------------



class EMSWidgetManager:
    def __init__(self, window: MainWindow):
        self.window = window

    def loadWidgets(self):
        self._loadTextboxes()
        self._loadButtons()
        self.window.checkboxes: Dict[str, QCheckBox] = { "disability": self.window.origin.findChild(QCheckBox, "disability_checkbox") }

    def _loadTextboxes(self):
        self.window.textboxes = {
            "employee_number": QtLineEdit(self.window.origin, "employee_number_textbox"),
            "name": QtLineEdit(self.window.origin, "name_textbox"),
            "address": QtLineEdit(self.window.origin, "address_textbox"),
            "rrn": QtLineEdit(self.window.origin, "rrn_textbox"),
            "phone_number": QtLineEdit(self.window.origin, "phone_number_textbox"),
            "disability": QtLineEdit(self.window.origin, "disability_textbox"),
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
        self.window.textboxes["employee_number"].setText(data["사원번호"])
        self.window.textboxes["name"].setText(data["이름"])
        self.window.textboxes["address"].setText(data["주소"])
        self.window.textboxes["rrn"].setText(data["주민번호"])
        self.window.textboxes["phone_number"].setText(data["전화번호"])
        disa = data["장애"]
        if disa == "":
            self.window.checkboxes["disability"].setChecked(False)
        else:
            self.window.checkboxes["disability"].setChecked(True)
        self.window.textboxes["disability"].setText(disa)
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
        for e in self.window.checkboxes.values():
            e.setChecked(False)


class EMS(MainWindow):
    def __init__(self):
        super().__init__(MainForm())
        self.__widgets = EMSWidgetManager(self)
        self.__widgets.loadWidgets()
        self.checkboxes["disability"].clicked.connect(self.clickDisabilityCheckbox)
        self._bindFunctionsToButtons()
        self.__is_editable: bool = False
        self.adding: bool = False
        self.__data = DataManager()
        self.__employee_data: Table = self.__data["employee_data"]
        self.__current_data: Table.Record = None
        self.textbox_default_style = self.textboxes["rrn"].origin.styleSheet()
        self.warning_label = QLabel("")
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
        self.origin.rrn_layout.addWidget(self.warning_label)
        self.warning_label.setHidden(True)
        self.buttons["edit"].setEnabled(False)
        self.buttons["leave"].setHidden(True)
        self.textboxes["rrn"].origin.textChanged.connect(self.__rrnDuplicateCheck)

    def __rrnDuplicateCheck(self):
        if not self.__is_editable:
            return
        # if self.adding:
        #     self.__rrnDuplicateCheckWhenAdding()
        #     return
        self.__rrnDuplicateCheckWhenEditing()


    def __rrnDuplicateCheckWhenEditing(self):
        rrn = self.textboxes["rrn"].getCurrentText()
        if rrn == "":
            self.textboxes["rrn"].setStyle(self.textbox_default_style)
            self.warning_label.setHidden(True)
            self.buttons["ok"].setEnabled(True)
            return
        for e in self.__employee_data:
            if rrn == e["주민번호"]:
                if e["사원번호"] == self.textboxes["employee_number"].getCurrentText():
                    continue
                self.warning_label.setHidden(False)
                self.warning_label.setStyleSheet("color: red; font: 9pt;")
                self.warning_label.setText("이미 존재하는 주민번호 입니다.")
                self.buttons["ok"].setEnabled(False)
                self.textboxes["rrn"].setStyle(self.textbox_default_style + ";border: 1px solid red; background-color: #FFDDDD;")
                return
        else:
            self.textboxes["rrn"].setStyle(self.textbox_default_style)
            self.warning_label.setHidden(True)
            self.buttons["ok"].setEnabled(True)

    def __rrnDuplicateCheckWhenAdding(self):
        rrn = self.textboxes["rrn"].getCurrentText()
        if rrn == "":
            self.textboxes["rrn"].setStyle(self.textbox_default_style)
            self.warning_label.setHidden(True)
            # self.buttons["ok"].setEnabled(True)
            return
        for e in self.__employee_data:
            if rrn == e["주민번호"]:
                self.warning_label.setHidden(False)
                self.warning_label.setStyleSheet("color: orange; font: 9pt;")
                self.warning_label.setText("기존 데이터에 덮어씁니다.")
                # self.buttons["ok"].setEnabled(False)
                self.textboxes["rrn"].setStyle(self.textbox_default_style + ";border: 1px solid orange; background-color: #FFF8DD;")
                return
        else:
            self.textboxes["rrn"].setStyle(self.textbox_default_style)
            self.warning_label.setHidden(True)
            # self.buttons["ok"].setEnabled(True)

    def setEditable(self, flag: bool):
        self.__is_editable = flag
        self.setTextboxesEditable(flag)
        self.setButtonsEditable(flag)
        self.setCheckboxesEditable(flag)

    def setTextboxesEditable(self, flag: bool):
        for e in self.textboxes.values():
            e.setEditable(flag)
        self.textboxes["employee_number"].setEditable(False)
        self.textboxes["pay"].setEditable(False)
        self.textboxes["duty"].setEditable(False)
        self.textboxes["workplace"].setEditable(False)
        if not self.checkboxes["disability"].isChecked():
            self.textboxes["disability"].setEditable(False)

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

    def setCheckboxesEditable(self, flag: bool):
        for e in self.checkboxes.values():
            e.setEnabled(flag)

    def clickCancelButton(self):
        ok = YesOrNoWindow("취소", "편집한 내용이 저장되지 않습니다.\n정말 취소 하시겠습니까?", self.origin).show()
        if ok:
            if self.adding:
                self.addCancel()
            else:
                self.editCancel()

    def clickDeleteButton(self):
        ok = YesOrNoWindow("삭제", "정말 삭제 하시겠습니까?", self.origin).show()
        if ok:
            self.deleteCurrentData()

    def deleteCurrentData(self):
        self.__employee_data.delete(self.__current_data["사원번호"])
        self.__current_data = None
        self.setEditable(False)
        self.buttons["edit"].setEnabled(False)
        self.buttons["leave"].setHidden(True)
        self.__widgets.clear()

    def clickEditButton(self):
        self.origin.is_saved = False
        self.editStart()
        
    def editStart(self):
        self.setEditable(True)

    def editCancel(self):
        if self.__current_data == None:
            self.__widgets.clear()
        else:
            self.__widgets.showData(self.__current_data)
        self.textboxes["rrn"].setStyle(self.textbox_default_style)
        self.warning_label.setHidden(True)
        self.setEditable(False)

    def editDone(self):
        self.setEditable(False)
        self.saveDatafromViewerToCurrentData()

    def saveDatafromViewerToCurrentData(self):
        self.__current_data["사원번호"] = self.textboxes["employee_number"].getCurrentText()
        self.__current_data["이름"] = self.textboxes["name"].getCurrentText()
        self.__current_data["주소"] = self.textboxes["address"].getCurrentText()
        self.__current_data["주민번호"] = self.textboxes["rrn"].getCurrentText()
        self.__current_data["전화번호"] = self.textboxes["phone_number"].getCurrentText()
        self.__current_data["계좌"] = self.textboxes["bank"][0].getCurrentText() + " " + self.textboxes["bank"][1].getCurrentText()
        self.__current_data["급여"] = self.textboxes["pay"].getCurrentText()
        self.__current_data["직책"] = self.textboxes["duty"].getCurrentText()
        self.__current_data["근무지"] = self.textboxes["workplace"].getCurrentText()
        self.__current_data["입사일"] = self.textboxes["start_date"].getCurrentText()
        self.__current_data["퇴사일"] = self.textboxes["end_date"].getCurrentText()

    def clickOkButton(self):
        if self.adding:
            self.addDone()
        else:
            self.editDone()

    def clickSaveButton(self):
        # self.__employee_data.save()
        self.origin.is_saved = True
        self.__data.save()
        toast = Toast("\n저장되었습니다\n", parent=self.origin)
        toast.setOpacity(0.7)
        toast.setFont(QFont("Arial", 12, weight=80))
        toast.setAlignment(Qt.AlignCenter)
        toast.show()

    def clickSaveToolButton(self):
        print("click save tool button")

    def clickAddButton(self):
        self.origin.is_saved = False
        self.addStart()

    def addStart(self):
        self.adding = True
        self.setEditable(True)
        self.__widgets.clear()
        self.buttons["delete"].setHidden(True)
        self.buttons["leave"].setHidden(True)
        today = datetime.now().date()
        self.textboxes["start_date"].setText(f"{today}")
        data = []
        for e in self.__employee_data:
            if int(e["사원번호"][0:4]) == today.year:
                data.append(int(e["사원번호"][5:8]))
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
        self.textboxes["rrn"].setStyle(self.textbox_default_style)
        self.warning_label.setHidden(True)
        self.adding = False
        self.setEditable(False)

    def addDone(self):
        self.__current_data = self.__employee_data.getNewEmptyRecord()
        self.saveDatafromViewerToCurrentData()
        self.buttons["leave"].setHidden(False)
        self.textboxes["rrn"].setStyle(self.textbox_default_style)
        self.warning_label.setHidden(True)
        self.adding = False
        self.setEditable(False)

    def clickLoadButton(self):
        self.popLoadWindow()

    def popLoadWindow(self):
        sub = EMSLoadWindow(self.__employee_data)
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
            key = self.__current_data["사원번호"]
        sub = EMSPayWindow(self.__data["pay_data"], key, self.__is_editable)
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
            key = self.__current_data["사원번호"]
        sub = EMSLeaveWindow(self.__data["leave_data"], key, self.__is_editable)
        sub.show()

    def clickDisabilityCheckbox(self):
        if self.checkboxes["disability"].isChecked():
            self.textboxes["disability"].setEditable(True)
        else:
            self.textboxes["disability"].setEditable(False)
            self.textboxes["disability"].setText("")