from Data import *

import json


class List(Data):
    def __init__(self, origin_source: str = None):
        self.__origin_source = origin_source
        if origin_source != None:
            origin_file = open(origin_source, 'r', encoding="utf-8")
            self.__data: list = json.load(origin_file)
            origin_file.close()

    def save(self):
        with open(self.__origin_source, 'w', encoding="UTF-8") as outfile:
            json.dump(self.__data, outfile, indent=4, ensure_ascii=False)

    def add(self, data):
        for e in self.__data:
            if data == e:
                # print(data + " is already exist")
                return
        self.__data.append(data)
        
    def data(self):
        return self.__data

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value):
        self.__data[index] = value


if __name__ == "__main__":
    data = List("./data/사업장.json")
    for e in data:
        print(e)
    data.add("무슨 상가")
    data.save()