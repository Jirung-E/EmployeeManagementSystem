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
#include <stdlib.h>


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







CSVData* csv_data;

void cpploadCSVData(const wchar_t* file_path) {
    csv_data = new CSVData { file_path };
}

const wchar_t* cppcsvGet(int row, const wchar_t* column) {
    return (*csv_data)[row][column];
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
}