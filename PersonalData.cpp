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


PersonalData::PersonalData(std::string name, std::string address, const Rrn& rrn, const PhoneNumber& phone_number, const BankAccount& bank_account) :
    name { name }, address { address }, rrn { rrn }, phone_number { phone_number }, bank_account { bank_account } {

}

PersonalData::PersonalData(const PersonalData& other) : PersonalData { other.name, other.address, other.rrn, other.phone_number, other.bank_account } {

}

PersonalData& PersonalData::operator=(const PersonalData& other) {
    name = other.name;
    address = other.address;
    rrn = other.rrn;
    phone_number = other.phone_number;
    bank_account = other.bank_account;

    return *this;
}

std::string PersonalData::get() const {
    std::string result = name + '\n';
    result += address + '\n';
    result += rrn.get() + '\n';
    result += phone_number.get() + '\n';
    result += bank_account.get();

    return result;
}
