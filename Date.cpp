#define _CRT_SECURE_NO_WARNINGS

#include "Date.h"

#include <ctime>
#include <format>


struct tm* Date::getCurrentTime() {
    time_t current_time = time(nullptr);
    struct tm* current_tm = localtime(&current_time);

    return current_tm;
}

Date::Date(std::string date) {
    if(date == "None" || date == "" || date == "-" || date == "--" || date == "0000-00-00" || date.length() < 10) {
        year = "";
        month = "";
        day = "";
        return;
    }
    struct tm t;
    t.tm_year = std::stoi(date.substr(0, 4)) - 1900;
    t.tm_mon = std::stoi(date.substr(4 + 1, 2)) - 1;
    t.tm_mday = std::stoi(date.substr(6 + 2, 2));
    t.tm_hour = 0;
    t.tm_min = 0;
    t.tm_sec = 0;
    time_t ti = mktime(&t);
    struct tm* tm = std::localtime(&ti);
    year = std::format("{:0>4d}", tm->tm_year + 1900);
    month = std::format("{:0>2d}", tm->tm_mon + 1);
    day = std::format("{:0>2d}", tm->tm_mday);
}

Date::Date() : Date { "" } {

}


std::string Date::get() const {
    if(year == "" || month == "" || day == "") {
        return "-";
    }
    return year + "-" + month + "-" + day;
}