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


Employee::Employee(const EmployeeData& employee_data) : employee_data { employee_data } {

}