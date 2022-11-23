#pragma once

#include <string>


class Date {
private:
    std::wstring year;
    std::wstring month;
    std::wstring day;

public:
    Date(std::wstring date = L"");

public:
    std::wstring get() const;

    static struct tm* getCurrentTime();
};