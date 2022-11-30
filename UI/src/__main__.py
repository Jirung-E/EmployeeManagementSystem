import ctypes
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

mainwindow = uic.loadUiType("../mainwindow.ui")[0]

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
            "employee_number": self.findChild(QLineEdit, "employee_number_textbox") ,
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
        self.button["load"].clicked.connect(loadData)

def emsSetUp(path):
    ems = ctypes.CDLL(path)                         # 필요시 try - except

    global getData
    global loadCSVData

    getData = ems['getData']
    getData.argtypes = [ ctypes.c_wchar_p ]
    getData.restype = ctypes.c_wchar_p

    loadCSVData = ems["loadCSVData"]
    loadCSVData.argtypes = [ ctypes.c_wchar_p ]

def loadData():
    loadCSVData("../../data.csv")
    # contents = getData("../../data.txt")
    # print(contents)
    # return contents



path = "../../x64/Release/EmployeeManagementSystem"        # 필요시 input
emsSetUp(path)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()