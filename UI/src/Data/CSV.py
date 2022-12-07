from Library.CLib import CSV


class CSVData:
    def __init__(self):
        pass

    def selectRow(self, index: int):
        CSV.selectRow(index)

    def getItem(self, column: str):
        return CSV.getItem(column)

    def loadData(self):
        CSV.loadData()


data = CSVData()
data.loadData()