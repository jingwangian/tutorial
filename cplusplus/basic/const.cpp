#include <iostream>
using namespace std;
/*
Defining Constants: #define vs const

#define:
    no memory to store in your program
    no type
    no scope, global value
    can't use sizeof
    can't take address

const:
    typed, scope


*/

#define H1 100;
static int const H2=120;
const int H3=300;

void print_const()
{
    const int H2=230;
    cout<<H2<<'\n';

    cout<<H3<<'\n';
}

void print_const2()
{
    cout<<H2<<'\n';

    cout<<H3;
}

int main(void)
{
    cout<<H1;
    #define H1 200;

    cout<<H1;

    const int H2 = 300;
    cout<<H2;

    print_const();
    print_const2();
    return 0;
}
