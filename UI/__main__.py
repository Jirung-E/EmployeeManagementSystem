import ctypes

from tkinter import *


def emsSetUp(path):
    ems = ctypes.CDLL(path)                         # 필요시 try - except

    global getData
    getData = ems['getData']

    getData.argtypes = [ ctypes.c_wchar_p ]
    getData.restype = ctypes.c_wchar_p

def loadData():
    contents = getData("../data.txt")
    print(contents)
    return contents
    

class MyWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("사원 관리 시스템")
        self.root.geometry("640x480")
        self.root.resizable(False, False)

        self.load_button = Button(self.root, text="load", command=self.loadButtonClick)
        self.load_button.pack()
        self.text_box = Text(self.root, width=50, height=10)
        self.text_box.pack()

    def loadButtonClick(self):
        contents = loadData()
        self.text_box.insert(END, contents)

    def run(self):
        self.root.mainloop()

path = "../x64/Release/EmployeeManagementSystem"        # 필요시 input
emsSetUp(path)
MyWindow().run()