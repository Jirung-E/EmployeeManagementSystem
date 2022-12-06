from PyQt5.QtWidgets import *
from PyQt5 import uic

from CSV import *

mainwindow = uic.loadUiType("./UI/mainwindow.ui")[0]

class Main(QMainWindow, mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.editable = False
        self.will_save = False
        self.__loadTextbox()
        self.__loadButton()
        # self.contents = Contents()
        # self.contents.add(self.textbox)
        # self.contents.setEditable(False)
        # self.button["edit"].setEnabled(False)

    def __loadTextbox(self):
        self.textbox = {
            "employee_number": self.findChild(QLineEdit, "employee_number_textbox"),
            "name": self.findChild(QLineEdit, "name_textbox"),
            "address": self.findChild(QLineEdit, "address_textbox"),
            "rrn": self.findChild(QLineEdit, "rrn_textbox"),
            "phone_number": self.findChild(QLineEdit, "phone_number_textbox"),
            "bank": self.findChild(QLineEdit, "bank_textbox"),
            "duty": self.findChild(QLineEdit, "duty_textbox"),
            "pay": self.findChild(QLineEdit, "pay_textbox"),
            "workplace": self.findChild(QLineEdit, "workplace_textbox"),
            "start_date": self.findChild(QLineEdit, "startdate_textbox"),
            "end_date": self.findChild(QLineEdit, "enddate_textbox"),
        }

    def __loadButton(self):
        self.button = {
            "edit": self.findChild(QPushButton, "edit_button"), 
            "save": self.findChild(QPushButton, "save_button"),
            "save_tool": self.findChild(QToolButton, "save_toolbutton"),
            "add": self.findChild(QPushButton, "add_button"),
            "load": self.findChild(QPushButton, "load_button"),
        }
        self.button["load"].clicked.connect(self.__buttonClick_load)

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
        employee, ok = QInputDialog.getItem(self, "선택", "선택하세요", employee_list, 0, False)
        if ok:
            data.selectRow(employee_list.index(employee) + 1)
            self.__show()

    def __show(self):
        self.textbox["employee_number"].setText(data.getItem("사원번호"))
        self.textbox["name"].setText(data.getItem("이름"))
        self.textbox["address"].setText(data.getItem("주소"))
        self.textbox["rrn"].setText(data.getItem("주민번호"))
        self.textbox["phone_number"].setText(data.getItem("전화번호"))
        self.textbox["bank"].setText(data.getItem("계좌"))
        self.textbox["duty"].setText(data.getItem("직책"))
        monthly_pay = sum(map(int, [ data.getItem("기본수당"), data.getItem("야간수당"), data.getItem("특수수당") ]))
        self.textbox["pay"].setText(str(monthly_pay))
        self.textbox["workplace"].setText(data.getItem("사업장"))
        self.textbox["start_date"].setText(data.getItem("입사일"))
        self.textbox["end_date"].setText(data.getItem("퇴사일"))