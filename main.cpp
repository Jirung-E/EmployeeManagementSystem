#include <iostream>

#include "Employee.h"

using namespace std;


int main() {
    //EmployeeNumber en;
    //cout << en.get() << endl;

    //string name = "김밥";
    //string addr = "여기도 저기시 위로구 아래로 24번길 53, 101동 1234호";

    //Rrn rrn { "123456-1234567" };
    //cout << rrn.get() << endl;

    //PhoneNumber pn { "010-1111-2222" };
    //cout << pn.get() << endl;

    //BankAccount ba { "우리", "1234-123-123123" };
    //cout << ba.get() << endl;

    //string duty = "경비원";

    //Pay pay { 2000000, 1000000, 1230000 };

    //string workplace = "PY TOWER";

    //Date start_date { "2022-06-02" };
    //cout << start_date.get() << endl;

    //Date end_date;
    //cout << end_date.get() << endl;

    EmployeeData ed { "data.txt" };
    cout << ed.get() << endl;
}