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


extern "C" {
    EXPORT int test() {
        return cpptest();
    }

    EXPORT const wchar_t* getData(const wchar_t* file_path) {
        return cppgetData(file_path);
    }
}

// https://afsdzvcx123.tistory.com/entry/C-csv-%ED%8C%8C%EC%9D%BC-%EC%9D%BD%EA%B8%B0-%EB%B0%8F-%ED%8C%8C%EC%8B%B1-%EB%B0%A9%EB%B2%95