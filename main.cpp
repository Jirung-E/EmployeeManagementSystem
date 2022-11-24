#include <iostream>
#include <locale>

using namespace std;

extern wchar_t* cppgetData(const wchar_t* file_path);


int main() {
    setlocale(LC_ALL, "");
    //locale::global(std::locale("kor"));
    //wcout.imbue(locale("kor"));

    wchar_t* ws = cppgetData(L"./data.txt");
    wcout << ws << endl;
}