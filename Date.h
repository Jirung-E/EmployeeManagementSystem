#pragma once

#include <string>


class Date {
private:
    std::string year;
    std::string month;
    std::string day;

public:
    Date(std::string date = "");

public:
    std::string get() const;

    static struct tm* getCurrentTime();
};