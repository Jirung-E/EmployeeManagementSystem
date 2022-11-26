#include "CSV.h"

#include <algorithm>

CSVData::CSVData() {
    
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
