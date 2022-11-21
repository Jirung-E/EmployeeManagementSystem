#include "Employee.h"

#include "Date.h"


EmployeeNumber::EmployeeNumber() : first { std::to_string(Date::getCurrentTime()->tm_year + 1900) }, last { "123" } {

}

EmployeeNumber::EmployeeNumber(std::string employee_number) : first { employee_number.substr(0, first_length) }, last { employee_number.substr(first_length+1, last_length) } {
    
}

std::string EmployeeNumber::get() const {
    return first + "-" + last;
}


Pay::Pay(int base, int allowance, int night) : base { base }, allowance { allowance }, night { night } {

}

int Pay::getMonthlyPay() const {
    return base + allowance + night;
}

std::string Pay::get() const {
    std::string result = std::to_string(base) + '\n';
    result += std::to_string(allowance) + '\n';
    result += std::to_string(night) + '\n';
    result += std::to_string(getMonthlyPay()) + '\n';

    return result;
}


EmployeeData::EmployeeData(std::string file_path) {
    loadData(file_path);
}


EmployeeData EmployeeData::loadData(std::string file_path) {
    std::ifstream ifs(file_path);
    if(ifs.fail()) {
        // error
        return *this;
    }
    std::string en;
    std::getline(ifs, en);
    employee_number = EmployeeNumber { en };

    std::string name;
    std::getline(ifs, name);
    std::string addr;
    std::getline(ifs, addr);
    std::string rrn;
    std::getline(ifs, rrn);
    std::string phone;
    std::getline(ifs, phone);
    std::string bank, number;
    std::getline(ifs, bank, ' ');
    std::getline(ifs, number, '\n');
    Rrn r { rrn };
    PhoneNumber p { phone };
    BankAccount b { bank, number };
    personal_data = PersonalData { name, addr, r, p, b };

    std::getline(ifs, duty);

    std::string p1, p2, p3;
    std::getline(ifs, p1);
    std::getline(ifs, p2);
    std::getline(ifs, p3);
    pay = Pay { std::stoi(p1), std::stoi(p2), std::stoi(p3) };

    std::getline(ifs, workplace);

    std::string sd, ed;
    std::getline(ifs, sd);
    std::getline(ifs, ed);
    start_work_date = Date { sd };
    end_work_date = Date { ed };

    ifs.close();

    return *this;
}

std::string EmployeeData::get() const {
    std::string result = employee_number.get() + '\n';
    result += personal_data.get() + '\n';
    result += duty + '\n';
    result += pay.get();
    result += workplace + '\n';
    result += start_work_date.get() + '\n';
    result += end_work_date.get() + '\n';

    return result;
}


Employee::Employee(const EmployeeData& employee_data) : employee_data { employee_data } {

}