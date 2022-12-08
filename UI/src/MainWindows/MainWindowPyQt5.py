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

from Data.CSV import *

data = CSVData()
data.loadData("./data.csv")


class EMS(MainWindow):
    def __init__(self):
        super().__init__(MainForm())
        self._loadTextboxes()
        self._loadButtons()
        self._bindFunctionsToButtons()
        self.__is_editable: bool = False
        self._setEditable(False)

    def _loadTextboxes(self):
        self.textboxes = {
            "employee_number": QtLineEdit(self.origin, "employee_number_textbox"),
            "name": QtLineEdit(self.origin, "name_textbox"),
            "address": QtLineEdit(self.origin, "address_textbox"),
            "rrn": QtLineEdit(self.origin, "rrn_textbox"),
            "phone_number": QtLineEdit(self.origin, "phone_number_textbox"),
            "bank": WidgetBox(QtLineEdit(self.origin, "bank_textbox_1"), QtLineEdit(self.origin, "bank_textbox_2")),
            "duty": QtLineEdit(self.origin, "duty_textbox"),
            "pay": QtLineEdit(self.origin, "pay_textbox"),
            "workplace": QtLineEdit(self.origin, "workplace_textbox"),
            "start_date": QtLineEdit(self.origin, "startdate_textbox"),
            "end_date": QtLineEdit(self.origin, "enddate_textbox"),
        }

    def _loadButtons(self):
        self.buttons = {
            "edit": QtButton(self.origin, "edit_button"), 
            "save": QtButton(self.origin, "save_button"),
            "save_tool": QtButton(self.origin, "save_toolbutton"),
            "add": QtButton(self.origin, "add_button"),
            "load": QtButton(self.origin, "load_button")
        }

    def _bindFunctionsToButtons(self):
        self.buttons["load"].bindFunction(self.__buttonClick_load)
        self.buttons["edit"].bindFunction(self.__buttonClick_edit)

    def _setEditable(self, flag: bool):
        self.__is_editable = flag
        if flag is True:
            self.buttons["edit"].setText("취소")
            self.buttons["save"].setText("확인")
        else:
            self.buttons["edit"].setText("수정")
            self.buttons["save"].setText("저장")
        for e in self.textboxes.values():
            e.setEditable(flag)

    def __buttonClick_edit(self):
        if self.__is_editable is True:
            self._setEditable(False)
        else:
            self._setEditable(True)

    def __buttonClick_load(self):
        self.__showLoadWindow()

    def __showLoadWindow(self):
        data.selectRow(0)
        header = f'[{data.getItem("사원번호")}] {data.getItem("이름")} ({data.getItem("사업장")})'
        employee_list = []
        for i in range(1, 10):
            data.selectRow(i)
            item = f'[{data.getItem("사원번호")}] {data.getItem("이름")} ({data.getItem("사업장")})'
            if item == header:
                break
            employee_list.append(item)
        employee, ok = QInputDialog.getItem(self.origin, "선택", "선택하세요", employee_list, 0, False)
        if ok:
            data.selectRow(employee_list.index(employee) + 1)
            self.__show()

    def __show(self):
        self.textboxes["employee_number"].setText(data.getItem("사원번호"))
        self.textboxes["name"].setText(data.getItem("이름"))
        self.textboxes["address"].setText(data.getItem("주소"))
        self.textboxes["rrn"].setText(data.getItem("주민번호"))
        self.textboxes["phone_number"].setText(data.getItem("전화번호"))
        bank_account = data.getItem("계좌").split(' ')
        self.textboxes["bank"][0].setText(bank_account[0])
        self.textboxes["bank"][1].setText(bank_account[1])
        self.textboxes["duty"].setText(data.getItem("직책"))
        monthly_pay = sum(map(int, [ data.getItem("기본수당"), data.getItem("야간수당"), data.getItem("특수수당") ]))
        self.textboxes["pay"].setText(str(monthly_pay))
        self.textboxes["workplace"].setText(data.getItem("사업장"))
        self.textboxes["start_date"].setText(data.getItem("입사일"))
        self.textboxes["end_date"].setText(data.getItem("퇴사일"))