#include <iostream>
using namespace std;

/*
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
\xhh                Hexadecimal number of one or more digits
*/

int main(void)
{
    cout<<"hello \\ world"<<endl;
    cout<<"hello \'world\'"<<endl;
    cout<<"hello \"world\""<<endl;
    cout<<"hello \"world\"\?"<<endl;
    cout<<"hello world\b e"<<endl;
    cout<<"hello world\f"<<endl;
    cout<<"hello world\rxxxx"<<endl;
    cout<<"hello world\nxxxx"<<endl;

    cout<<"hello world\ooo"<<endl;
    return 0;
}
