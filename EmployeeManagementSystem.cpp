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

std::wstring setUp_str(const wchar_t* file_path) {
    std::wstring path { file_path };
    EmployeeData ed { path };
    return ed.get();
}

wchar_t* setUp(const wchar_t* file_path) {
    std::wstring wstr { setUp_str(file_path) };
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
        str = setUp(file_path);
        return str;
    }
}