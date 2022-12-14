from Data.Data import Data

import csv


class DataTable(Data):
    def __init__(self, origin_source: str = None):
        self.__origin_source = origin_source
        self.__attributes = {}   # column_name
        if origin_source != None:
            origin_file = open(origin_source, 'r', encoding="utf-8")
            self.__data = [ data for data in csv.reader(origin_file) ]
            for i in range(0, len(self.__data[0])):
                self.__attributes[self.__data[0][i]] = i
            self.__data.pop(0)
            origin_file.close()

    class Record(Data):
        def __init__(self, attributes, data):
            self.__attributes = attributes
            self.__data = data

        def data(self):
            return self.__data

        def __getitem__(self, attribute: str):
            return self.__data[self.__attributes[attribute]]

    def save(self):
        origin_file = open(self.__origin_source, 'w', encoding="utf-8", newline='')
        writer = csv.writer(origin_file)
        writer.writerow(self.getAttributes())
        writer.writerows(self.__data)
        origin_file.close()
        
    def getField(self, attribute: str):
        field = []
        for e in self.__data:
            field.append(e[self.__attributes[attribute]])
        return field

    def getRecord(self, index: int):
        return self.__data[index]

    def __getitem__(self, index: int):
        return DataTable.Record(self.__attributes, self.__data[index])

    def getAttributes(self):
        return list(self.__attributes.keys())

    def getNumOfRecords(self):
        return len(self.__data)


if __name__ == "__main__":
    data = DataTable("./data/data.csv")
    print(data.getAttributes())
    print(data.getField("주민번호"))
    print(data.getRecord(1))
    print(data[1].data())
    print(data[1]["이름"])
    data.save()