#include <iostream>
#include <locale>

using namespace std;

extern wchar_t* setUp(const wchar_t* file_path);
extern wstring setUp_str(const wchar_t*);


int main() {
    setlocale(LC_ALL, "");
    //locale::global(std::locale("kor"));
    //wcout.imbue(locale("kor"));

    wchar_t* ws = setUp(L"./data.txt");
    wcout << ws << endl;

    wstring view { setUp_str(L"./data.txt") };
    wcout << view << endl;
}