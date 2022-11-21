#pragma once

#include <string>

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

public:
    std::string get() const;
};


class Pay {
private:
    int base;
    int allowance;
    int night;

public:
    Pay(int base, int allowance, int night);
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
};


class Employee {
private:
    EmployeeData employee_data;
public:
    Employee(const EmployeeData& employee_data);
};