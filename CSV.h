#pragma once

#include <string>
#include <list>

#include "DataReader.h"


class CSVData {
private:
    std::list<std::list<std::wstring>> data;

    static const wchar_t separator = L',';

public:
    CSVData(const std::wstring& contents = L"");

    std::list<std::wstring> operator[](const std::wstring& column_name);
    std::list<std::wstring>& operator[](int index);

public:
    //void initialize();
};


class CSVReader : public DataReader {
public:
    std::wstring read(const std::wstring& file_path);
};