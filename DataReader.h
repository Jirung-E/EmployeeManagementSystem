#pragma once

#include <string>


class DataReader {
public:
    virtual std::wstring read(const std::wstring& file_name) = 0;
};