#include <iostream>

#include "Employee.h"

using namespace std;


int main() {
    //EmployeeNumber en;
    //cout << en.get() << endl;

    //string name = "���";
    //string addr = "���⵵ ����� ���α� �Ʒ��� 24���� 53, 101�� 1234ȣ";

    //Rrn rrn { "123456-1234567" };
    //cout << rrn.get() << endl;

    //PhoneNumber pn { "010-1111-2222" };
    //cout << pn.get() << endl;

    //BankAccount ba { "�츮", "1234-123-123123" };
    //cout << ba.get() << endl;

    //string duty = "����";

    //Pay pay { 2000000, 1000000, 1230000 };

    //string workplace = "PY TOWER";

    //Date start_date { "2022-06-02" };
    //cout << start_date.get() << endl;

    //Date end_date;
    //cout << end_date.get() << endl;

    EmployeeData ed { "data.txt" };
    cout << ed.get() << endl;
}