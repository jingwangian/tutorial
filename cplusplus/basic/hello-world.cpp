#include <iostream>
using namespace std;
void endianess_test(void);

int main() {
   cout << "Hello World"<<endl;
   endianess_test();
   return 0;
}

void endianess_test()
{
    int n = 1;
    // little endian if true
    if(*(char *)&n == 1)
        cout<<"little endian\n";
    else
        cout<<"big endian\n";
}
