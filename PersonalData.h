#pragma once

#include <string>


class Rrn {
private:
    std::string first;
    std::string last;
    const static int first_length = 6;
    const static int last_length = 7;

public:
    Rrn(std::string rrn);
    Rrn() = default;

public:
    std::string get() const;
};

class PhoneNumber {
private:
    std::string prefix;
    std::string first;
    std::string last;
    const static int prefix_length = 3;
    const static int first_length = 4;
    const static int last_length = 4;

public:
    PhoneNumber(std::string phone_number);
    PhoneNumber() = default;

public:
    std::string get() const;
};

class BankAccount {
private:
    std::string bank;
    std::string number;

public:
    BankAccount(std::string bank, std::string number);
    BankAccount() = default;

public:
    std::string get() const;
};

class PersonalData {
private:
    std::string name;
    std::string address;
    Rrn rrn;
    PhoneNumber phone_number;
    BankAccount bank_account;

public:
    PersonalData(std::string name, std::string address, const Rrn& rrn, const PhoneNumber& phone_number, const BankAccount& bank_account);
    PersonalData(const PersonalData& other);
    PersonalData() = default;
    PersonalData& operator=(const PersonalData& other);

public:
    std::string get() const;
};