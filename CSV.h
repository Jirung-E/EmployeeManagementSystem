#pragma once

#include <string>
#include <list>
//#include "DataReader.h"


class CSVData {
private:
    std::list<std::list<std::wstring>> data;

public:
    CSVData();

    std::list<std::wstring> operator[](const std::wstring& column_name);
    std::list<std::wstring>& operator[](int index);

public:
    //void initialize();
};



//class CSVReader : public DataReader {
//public:
//    CSVReader();
//
//public:
//    std::wstring read(const std::wstring& file_name);
//};