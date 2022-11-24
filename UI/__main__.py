import ctypes

from tkinter import *


class MyWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("사원 관리 시스템")
        self.root.geometry("640x480")
        self.root.resizable(False, False)

        self.load_button = Button(self.root, text="load", command=self.loadData)
        self.load_button.pack()
        self.text_box = Text(self.root, width=50, height=10)
        self.text_box.pack()

    def loadData(self):
        ems = ctypes.CDLL("../x64/Release/EmployeeManagementSystem")
        SetUp = ems['SetUp']

        SetUp.argtypes = [ ctypes.c_wchar_p ]
        SetUp.restype = ctypes.c_wchar_p

        contents = SetUp("../data.txt")
        print(contents)
        self.text_box.insert(END, contents)

    def run(self):
        self.root.mainloop()

MyWindow().run()