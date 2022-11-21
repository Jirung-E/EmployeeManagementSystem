#pragma once

#include <string>
#include <fstream>

#include "PersonalData.h"
#include "Date.h"


class EmployeeNumber {
private:
    std::string first;
    std::string last;
    const static int first_length = 4;
    const static int last_length = 3;

public:
    EmployeeNumber();
    EmployeeNumber(std::string employee_number);
    EmployeeNumber& operator=(const EmployeeNumber& other) = default;

public:
    std::string get() const;
};


class Pay {
private:
    int base;
    int allowance;
    int night;

public:
    Pay(int base = 0, int allowance = 0, int night = 0);

public:
    int getMonthlyPay() const;
    std::string get() const;
};


class EmployeeData {
private:
    EmployeeNumber employee_number;
    PersonalData personal_data;
    std::string duty;
    Pay pay;
    std::string workplace;
    Date start_work_date;
    Date end_work_date;

public:
    EmployeeData(std::string file_path);

public:
    EmployeeData loadData(std::string file_path);

    std::string get() const;
};


class Employee {
private:
    EmployeeData employee_data;
public:
    Employee(const EmployeeData& employee_data);
};