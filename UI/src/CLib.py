import ctypes


def emsSetUp(path):
    ems = ctypes.CDLL(path)                         # 필요시 try - except

    global getData
    global loadCSVData
    global csvSelectRow
    global csvGetItem

    getData = ems['getData']
    getData.argtypes = [ ctypes.c_wchar_p ]
    getData.restype = ctypes.c_wchar_p

    loadCSVData = ems["loadCSVData"]
    loadCSVData.argtypes = [ ctypes.c_wchar_p ]

    csvSelectRow = ems["csvSelectRow"]
    csvSelectRow.argtypes = [ ctypes.c_int ]

    csvGetItem = ems['csvGetItem']
    csvGetItem.argtypes = [ ctypes.c_wchar_p ]
    csvGetItem.restype = ctypes.c_wchar_p


def selectRow(index: ctypes.c_int):
    csvSelectRow(index)

def getItem(column: ctypes.c_wchar_p):
    return csvGetItem(column)

def loadData():
    loadCSVData("./data.csv")
    # contents = getData("../../data.txt")
    # print(contents)
    # return contents


path = "./x64/Release/EmployeeManagementSystem.dll"
emsSetUp(path)