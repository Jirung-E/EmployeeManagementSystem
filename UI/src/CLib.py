import ctypes


def emsSetUp(path):
    ems = ctypes.CDLL(path)                         # �ʿ�� try - except

    global getData
    global loadCSVData
    global csvSelectRow
    global csvGetItem
    global csvSetItem

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

    csvSetItem = ems['csvSetItem']
    csvSetItem.argtypes = [ ctypes.c_wchar_p, ctypes.c_wchar_p ]


class CSV:
    @staticmethod
    def selectRow(index: ctypes.c_int):
        csvSelectRow(index)

    @staticmethod
    def getItem(column: ctypes.c_wchar_p):
        return csvGetItem(column)

    @staticmethod
    def setItem(column: ctypes.c_wchar_p, data: ctypes.c_wchar_p):
        return csvSetItem(column, data)

    @staticmethod
    def loadData():
        loadCSVData("./data.csv")
        # contents = getData("../../data.txt")
        # print(contents)
        # return contents


path = "./x64/Release/EmployeeManagementSystem.dll"
# path = "../../x64/Release/EmployeeManagementSystem.dll"
emsSetUp(path)


if __name__ == "__main__":
    print("CLib.py - Test Start")
    print("loadData:")
    CSV.loadData()
    print("selectRow:")
    CSV.selectRow(1)
    print("getItem:")
    print(CSV.getItem("사원번호"))
    print("setItem")
    CSV.setItem("사원번호", "2022-987")
    print("getItem:")
    print(CSV.getItem("사원번호"))