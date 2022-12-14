from Data.Data import Data

# from Library.CLib import CSV

import csv

with open('eggs.csv', 'r', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))
        

class CSVData(Data):
    def __init__(self):
        pass

    def loadData(self, file_path):
        pass

    def selectRow(self, index: int):
        pass

    def __getitem__(self, column_name: str):
        pass

    def numOfRows(self):
        pass


# class CSVData(Data):
#     def __init__(self):
#         pass

#     def loadData(self, file_path):
#         CSV.loadData(file_path)

#     def selectRow(self, index: int):
#         CSV.selectRow(index)

#     def __getitem__(self, column_name: str):
#         return CSV.getItem(column_name)

#     def numOfRows(self):
#         return 3