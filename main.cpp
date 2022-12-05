#include <iostream>
#include <locale>

#include "CSV.h"
#include "DataReader.h"

using namespace std;


extern "C" {
    int test();
    const wchar_t* getData(const wchar_t* file_path);
    void loadCSVData(const wchar_t* file_path);
    void csvSelectRow(int index);
    const wchar_t* csvGetItem(const wchar_t* column);
}


int main() {
    setlocale(LC_ALL, "");

    cout << test() << endl;
    wcout << getData(L"./data.txt") << endl;
    loadCSVData(L"./data.csv");
    csvSelectRow(2);
    wcout << csvGetItem(L"계좌") << endl;
}