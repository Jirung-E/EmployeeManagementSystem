#pragma once

#include <string>
#include <fstream>

#include "PersonalData.h"
#include "Date.h"


class EmployeeNumber {
private:
    std::wstring first;
    std::wstring last;
    const static int first_length = 4;
    const static int last_length = 3;

public:
    EmployeeNumber();
    EmployeeNumber(std::wstring employee_number);
    EmployeeNumber& operator=(const EmployeeNumber& other) = default;

public:
    std::wstring get() const;
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
    std::wstring get() const;
};


class EmployeeData {
private:
    EmployeeNumber employee_number;
    PersonalData personal_data;
    std::wstring duty;
    Pay pay;
    std::wstring workplace;
    Date start_work_date;
    Date end_work_date;

public:
    EmployeeData(std::wstring file_path);

public:
    EmployeeData loadData(std::wstring file_path);

    std::wstring get() const;
};


class Employee {
private:
    EmployeeData employee_data;
public:
    Employee(const EmployeeData& employee_data);
};