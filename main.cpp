#pragma warning(disable:4996)

#include <iostream>
#include <locale>
#include <sstream>
#include <codecvt>
#include <fstream>

#include "CSV.h"
#include "DataReader.h"

using namespace std;

extern wchar_t* cppgetData(const wchar_t* file_path);


int main() {
    setlocale(LC_ALL, "");
    //locale::global(std::locale("kor"));
    //wcout.imbue(locale("kor"));

    std::wifstream wif { L"./data.csv" };
    wif.imbue(std::locale(std::locale::empty(), new std::codecvt_utf8<wchar_t>));
    std::wstringstream wss;
    wss << wif.rdbuf();
    wcout << wss.str() << endl;

    wchar_t* ws = cppgetData(L"./data.txt");
    wcout << ws << endl;

    DataReader* reader = new CSVReader;
    CSVData data { reader->read(L"./data.csv") };

    cout << endl;

    cout << "data[이름]" << endl;
    for(const wstring& e : data[L"이름"]) {
        wcout << e << endl;
    }
    cout << endl;

    cout << "data[1]" << endl;
    for(const wstring& e : data[1]) {
        wcout << e << endl;
    }
}