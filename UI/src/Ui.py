from PyQt5.QtWidgets import *
from PyQt5 import uic

from CLib import *

mainwindow = uic.loadUiType("./UI/mainwindow.ui")[0]

class MainWindow(QMainWindow, mainwindow):
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
        loadData()
        selectRow(2)
        self.textbox["employee_number"].setText(getItem("사원번호"))
        self.textbox["name"].setText(getItem("이름"))
        self.textbox["address"].setText(getItem("주소"))