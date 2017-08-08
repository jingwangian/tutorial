#include <iostream>
using namespace std;

int sum(int a, int b=20, int c = 100)
{
   int result;

   result = a + b + c;

   return (result);
}

int main () {
   // local variable declaration:
   int a = 100;
   int b = 200;
   int c = 300;
   int result;

   // calling a function to add the values.
   result = sum(a, b, c);
   cout << "Total value is :" << result << endl;


   // calling a function to add the values.
   result = sum(a, b);
   cout << "Total value is :" << result << endl;

   // calling a function again as follows.
   result = sum(a);
   cout << "Total value is :" << result << endl;

   return 0;
}
