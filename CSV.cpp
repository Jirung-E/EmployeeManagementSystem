#pragma warning(disable:4996)

#include "CSV.h"

#include <algorithm>
#include <fstream>
#include <sstream>
#include <locale>
#include <iostream>
#include <codecvt>


CSVData::CSVData(const std::wstring& contents) {
    std::locale::global(std::locale("kor"));
    std::wistringstream wiss { contents };
    std::wstring buff;

    std::list<std::wstring> rows;
    while(std::getline(wiss, buff)) {
        rows.push_back(buff);
    }

    for(const std::wstring& e : rows) {
        std::list<std::wstring> row;
        std::wistringstream ss { e };
        while(std::getline(ss, buff, separator)) {
            row.push_back(buff);
        }
        data.push_back(row);
    }
}


std::list<std::wstring> CSVData::operator[](const std::wstring& column_name) {
    std::list<std::wstring> result;
    std::list<std::wstring>::iterator it = std::find(data.front().begin(), data.front().end(), column_name);
    if(it == data.front().end()) {
        return result;
    }
    int index = 0;
    for(std::list<std::wstring>::iterator i=data.front().begin(); i!=it; ++i) {
        ++index;
    }
    for(std::list<std::wstring>& row : data) {
        int id=0;
        for(std::wstring& e : row) {
            if(id == index) {
                result.push_back(e);
            }
            ++id;
        }
    }
    return result;
}

std::list<std::wstring>& CSVData::operator[](int index) {
    int i=0;
    for(std::list<std::wstring>& e : data) {
        if(i == index) {
            return e;
        }
        ++i;
    }
    return data.front();
}


std::wstring CSVReader::read(const std::wstring& file_path) {
    std::wifstream ifs { file_path };

    ifs.imbue(std::locale(std::locale::empty(), new std::codecvt_utf8<wchar_t>));

    std::wstringstream wss;
    wss << ifs.rdbuf();
    //std::wcout << wss.str() << std::endl;

    return wss.str();
}