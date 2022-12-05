#ifdef _MSC_VER
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#include <wchar.h>


extern int cpptest(void);
extern wchar_t* cppgetData(const wchar_t* file_path);
extern void cpploadCSVData(const wchar_t* file_path);
extern void cppcsvSelectRow(int index);
extern const wchar_t* cppcsvGetItem(const wchar_t* column);


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