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

Integer literals
------------------------
    212         // Legal
    215u        // Legal
    0xFeeL      // Legal
    078         // Illegal: 8 is not an octal digit
    032UU       // Illegal: cannot repeat a suffix
    85         // decimal
    0213       // octal
    0x4b       // hexadecimal
    30         // int
    30u        // unsigned int
    30l        // long
    30ul       // unsigned long

Floating-point literals
------------------------
    3.14159       // Legal
    314159E-5L    // Legal
    510E          // Illegal: incomplete exponent
    210f          // Illegal: no decimal or exponent
    .e55          // Illegal: missing integer or fraction

Character literals
------------------------
    Character literals are enclosed in single quotes.

    plain (narrow) character: 'x'
    wider character: L'x', should be stored in wchar_t type of variable. L can only be uppercase only.
    escape sequence: e.g., '\t'
    universal character: e.g., '\u02C0'

Escape sequence
------------------------
    Escape sequence     Meaning
    \\                  \ character
    \'                  ' character
    \"                  " character
    \?                  ? character
    \a                  Alert or bell
    \b                  Backspace
    \f                  Form feed
    \n                  Newline
    \r                  Carriage return
    \t                  Horizontal tab
    \v                  Vertical tab
    \ooo                Octal number of one to three digits
    \xhh . . .          Hexadecimal number of one or more digits

String literals
------------------------
    String literals are enclosed in double quotes. A string contains characters that are similar to character literals: plain characters, escape sequences, and universal characters.

    You can break a long line into multiple lines using string literals and separate them using whitespaces.
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

void pirnt_const_value()
{
    int i1 = 100;   //decimal value
    int i2 = 0100;  //octal value
    int i3 = 0x100; //hexadecimal value
    int i4 = 30u;   //unsigned int
    int i5 = 30l;   //long int
    int i6 = 30ul;

    cout<<"pirnt_const_value"<<endl;

    cout<<"i1:"<<i1<<endl;
    cout<<"i2:"<<i2<<endl;
    cout<<"i3:"<<i3<<endl;
    cout<<"i4:"<<i4<<endl;
    cout<<"i5:"<<i5<<endl;
    cout<<"i6:"<<i6<<endl;
}

void print_string_literal()
{
    cout<<"hello, \
    \
    dear"<<endl;
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
    pirnt_const_value();
    print_string_literal();
    return 0;
}
