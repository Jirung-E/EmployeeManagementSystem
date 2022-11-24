#ifdef _MSC_VER
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#pragma warning(disable:4996)

#include "Employee.h"

#include <locale>
#include <cwchar>
#include <iostream>
#include <stdlib.h>


static wchar_t* wcharstr;


int test() {
    return 123;
}

wchar_t* getData(const wchar_t* file_path) {
    std::wstring wstr { EmployeeData { std::wstring { file_path } }.get() };
    wcharstr = new wchar_t[wstr.length()];
    wcscpy(wcharstr, wstr.c_str());
    return wcharstr;
}


extern "C" {
    EXPORT int Test() {
        return test();
    }

    EXPORT wchar_t* str;        // lifetime 문제 때문에 전역변수 선언

    EXPORT const wchar_t* SetUp(const wchar_t* file_path) {
        str = getData(file_path);
        return str;
    }
}