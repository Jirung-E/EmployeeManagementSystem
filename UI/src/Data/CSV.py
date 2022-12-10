from Library.CLib import CSV


class CSVData:
    def __init__(self):
        pass

    def loadData(self, file_path):
        CSV.loadData(file_path)

    def selectRow(self, index: int):
        CSV.selectRow(index)

    def __getitem__(self, column_name: str):
        return CSV.getItem(column_name)

    def numOfRows(self):
        return 10