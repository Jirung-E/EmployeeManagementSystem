#pragma once

#include <string>


class Rrn {
private:
    std::wstring first;
    std::wstring last;
    const static int first_length = 6;
    const static int last_length = 7;

public:
    Rrn(std::wstring rrn);
    Rrn() = default;

public:
    std::wstring get() const;
};

class PhoneNumber {
private:
    std::wstring prefix;
    std::wstring first;
    std::wstring last;
    const static int prefix_length = 3;
    const static int first_length = 4;
    const static int last_length = 4;

public:
    PhoneNumber(std::wstring phone_number);
    PhoneNumber() = default;

public:
    std::wstring get() const;
};

class BankAccount {
private:
    std::wstring bank;
    std::wstring number;

public:
    BankAccount(std::wstring bank, std::wstring number);
    BankAccount() = default;

public:
    std::wstring get() const;
};

class PersonalData {
private:
    std::wstring name;
    std::wstring address;
    Rrn rrn;
    PhoneNumber phone_number;
    BankAccount bank_account;

public:
    PersonalData(std::wstring name, std::wstring address, const Rrn& rrn, const PhoneNumber& phone_number, const BankAccount& bank_account);
    PersonalData(const PersonalData& other);
    PersonalData() = default;
    PersonalData& operator=(const PersonalData& other);

public:
    std::wstring get() const;
};