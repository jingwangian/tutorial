/*
Array pass to function:
-------------------
    Way-1: Formal parameters as a pointer as follows:

        void myFunction(int *param) { .... }

    Way-2: Formal parameters as a sized array as follows:

        void myFunction(int param[10]) { .... }

    Way-3: Formal parameters as an unsized array as follows:

        void myFunction(int param[]) { .... }

Array get from function:
-------------------
    C++ does not allow to return an entire array as an argument to a function. However, you can return a pointer to an array by specifying the array's name without an index.

    If you want to return a single-dimension array from a function, you would have to declare a function returning a pointer as in the following example:
        int * myFunction() {}
*/

#include <iostream>
using namespace std;

// function declaration:
double getAverage(int arr[], int size);

int main ()
{
   // an int array with 5 elements.
   int balance[5] = {1000, 2, 3, 17, 50};
   double avg;

   // pass pointer to the array as an argument.
   avg = getAverage( balance, 5 ) ;

   // output the returned value
   cout << "Average value is: " << avg << endl;

   return 0;
}


double getAverage(int arr[], int size)
{
   int    i, sum = 0;
   double avg;

   for (i = 0; i < size; ++i)
   {
      sum += arr[i];
   }

   avg = double(sum) / size;

   return avg;
}
