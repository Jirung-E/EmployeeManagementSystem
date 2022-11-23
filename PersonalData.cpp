#include "PersonalData.h"


Rrn::Rrn(std::wstring rrn) : first { rrn.substr(0, first_length) }, last { rrn.substr(first_length + 1, last_length) } {

}

std::wstring Rrn::get() const {
    return first + L"-" + last;
}


PhoneNumber::PhoneNumber(std::wstring phone_number) : prefix { phone_number.substr(0, prefix_length) },
first { phone_number.substr(prefix_length + 1, first_length) },
last { phone_number.substr(prefix_length + 1 + first_length + 1, last_length) } {

}

std::wstring PhoneNumber::get() const {
    return prefix + L"-" + first + L"-" + last;
}

BankAccount::BankAccount(std::wstring bank, std::wstring number) : bank { bank }, number { number } {

}

std::wstring BankAccount::get() const {
    return bank + L" " + number;
}


PersonalData::PersonalData(std::wstring name, std::wstring address, const Rrn& rrn, const PhoneNumber& phone_number, const BankAccount& bank_account) :
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

std::wstring PersonalData::get() const {
    std::wstring result = name + L'\n';
    result += address + L'\n';
    result += rrn.get() + L'\n';
    result += phone_number.get() + L'\n';
    result += bank_account.get();

    return result;
}
