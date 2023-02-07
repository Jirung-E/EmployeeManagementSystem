from Data import *

from typing import Dict


class DataManager:
    def __init__(self):
        self.__path = "./data/"
        self.__data: Dict[str, Data] = {
            "employee_data": Table(self.__path + "직원정보.csv"),
            "pay_data": Table(self.__path + "급여.csv"),
            "leave_data": Table(self.__path + "휴가.csv"),
            "workplace_data": List(self.__path + "사업장.json"),
            "duty_data": List(self.__path + "직책.json"),
        }

    def save(self):
        for e in self.__data.values():
            e.save()

    def __getitem__(self, attribute: str):
        return self.__data[attribute]