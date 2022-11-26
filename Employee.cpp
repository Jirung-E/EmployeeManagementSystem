#pragma warning(disable : 4996)

#include "Employee.h"

#include "Date.h"

#include <iostream>


EmployeeNumber::EmployeeNumber() : first { std::to_wstring(Date::getCurrentTime()->tm_year + 1900) }, last { L"123" } {

}

EmployeeNumber::EmployeeNumber(std::wstring employee_number) : first { employee_number.substr(0, first_length) }, last { employee_number.substr(first_length+1, last_length) } {
    
}

std::wstring EmployeeNumber::get() const {
    return first + L"-" + last;
}


Pay::Pay(int base, int allowance, int night) : base { base }, allowance { allowance }, night { night } {

}

int Pay::getMonthlyPay() const {
    return base + allowance + night;
}

std::wstring Pay::get() const {
    std::wstring result = std::to_wstring(base) + L'\n';
    result += std::to_wstring(allowance) + L'\n';
    result += std::to_wstring(night) + L'\n';
    result += std::to_wstring(getMonthlyPay()) + L'\n';

    return result;
}


EmployeeData::EmployeeData(std::wstring file_path) {
    loadData(file_path);
}


EmployeeData EmployeeData::loadData(std::wstring file_path) {
    std::locale::global(std::locale("kor"));
    std::wifstream ifs(file_path);
    if(ifs.fail()) {
        printf("Error: No such file.");
        return *this;
    }
    std::wstring en;
    std::getline(ifs, en);
    employee_number = EmployeeNumber { en };

    std::wstring name;
    std::getline(ifs, name);
    std::wstring addr;
    std::getline(ifs, addr);
    std::wstring rrn;
    std::getline(ifs, rrn);
    std::wstring phone;
    std::getline(ifs, phone);
    std::wstring bank, number;
    std::getline(ifs, bank, L' ');
    std::getline(ifs, number, L'\n');
    Rrn r { rrn };
    PhoneNumber p { phone };
    BankAccount b { bank, number };
    personal_data = PersonalData { name, addr, r, p, b };

    std::getline(ifs, duty);

    std::wstring p1, p2, p3;
    std::getline(ifs, p1);
    std::getline(ifs, p2);
    std::getline(ifs, p3);
    pay = Pay { std::stoi(p1), std::stoi(p2), std::stoi(p3) };

    std::getline(ifs, workplace);

    std::wstring sd, ed;
    std::getline(ifs, sd);
    std::getline(ifs, ed);
    start_work_date = Date { sd };
    end_work_date = Date { ed };

    ifs.close();

    return *this;
}

std::wstring EmployeeData::get() const {
    std::wstring result = std::wstring { employee_number.get() }.append(L"\n");
    result.append(std::wstring { personal_data.get() });
    result += L"\n";
    result += std::wstring { pay.get() };
    result += std::wstring { workplace } + L'\n';
    result += std::wstring { start_work_date.get() } + L'\n';
    result += std::wstring { end_work_date.get() } + L'\n';

    return result;
}


Employee::Employee(const EmployeeData& employee_data) : employee_data { employee_data } {

}