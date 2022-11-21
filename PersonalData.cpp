#include "PersonalData.h"


Rrn::Rrn(std::string rrn) : first { rrn.substr(0, first_length) }, last { rrn.substr(first_length + 1, last_length) } {

}

std::string Rrn::get() const {
    return first + "-" + last;
}


PhoneNumber::PhoneNumber(std::string phone_number) : prefix { phone_number.substr(0, prefix_length) },
first { phone_number.substr(prefix_length + 1, first_length) },
last { phone_number.substr(prefix_length + 1 + first_length + 1, last_length) } {

}

std::string PhoneNumber::get() const {
    return prefix + "-" + first + "-" + last;
}

BankAccount::BankAccount(std::string bank, std::string number) : bank { bank }, number { number } {

}

std::string BankAccount::get() const {
    return bank + " " + number;
}