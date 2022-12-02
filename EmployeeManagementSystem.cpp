#ifdef _MSC_VER
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#pragma warning(disable:4996)

#include "Employee.h"
#include "CSV.h"

#include <locale>
#include <cwchar>
#include <iostream>
#include <codecvt>


static wchar_t* wcharstr;                   // lifetime 문제 때문에 전역변수 선언


int cpptest() {
    return 123;
}

wchar_t* cppgetData(const wchar_t* file_path) {
    std::wstring wstr { EmployeeData { std::wstring { file_path } }.get() };
    wcharstr = new wchar_t[wstr.length()];
    wcscpy(wcharstr, wstr.c_str());
    return wcharstr;
}






DataReader* reader;
CSVData csv_data;
std::list<std::wstring>* current_data;
int current_index;


void cpploadCSVData(const wchar_t* file_path) {
    reader = new CSVReader { };
    std::wcout.imbue(std::locale("kor"));
    //std::wcout << L"내용:" << reader->read(file_path) << std::endl;
    std::wstring contents { reader->read(file_path) };
    //std::cout << "?>?????" << std::endl;

    //std::wcout << L"contents: " << std::endl;
    //std::wcout << contents << std::endl;
    csv_data = CSVData { contents };
}

void cppcsvSelectRow(int index) {
    current_index = index;
    current_data = &(csv_data[index]);
}

const wchar_t* cppcsvGetItem(const wchar_t* column) {
    int i=0;
    for(const std::wstring& e : csv_data[0]) {
        if(column == e) {
            //std::wcout << column << std::endl;
            //std::wcout << e << std::endl;
            break;
        }
        ++i;
    }
    int index=0;
    for(const std::wstring& e : *current_data) {
        if(i == index) {
            //std::wcout << e << std::endl;
            return e.c_str();
        }
        ++index;
    }
    return L"";
}


extern "C" {
    EXPORT int test() {
        return cpptest();
    }

    EXPORT const wchar_t* getData(const wchar_t* file_path) {
        return cppgetData(file_path);
    }

    EXPORT void loadCSVData(const wchar_t* file_path) {
        cpploadCSVData(file_path);
    }

    EXPORT void csvSelectRow(int index) {
        cppcsvSelectRow(index);
    }

    EXPORT const wchar_t* csvGetItem(const wchar_t* column) {
        return cppcsvGetItem(column);
    }
}