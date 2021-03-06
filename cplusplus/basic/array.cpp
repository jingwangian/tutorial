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

Declaring Arrays
-------------------
type arrayName [ arraySize ];

Initializing Arrays
-------------------
double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};
double balance[] = {1000.0, 2.0, 3.4, 7.0, 50.0};

Two-Dimensional Arrays
-------------------
type arrayName [ x ][ y ];

int a[3][4] = {
   {0, 1, 2, 3} ,   //  initializers for row indexed by 0
   {4, 5, 6, 7} ,   //  initializers for row indexed by 1
   {8, 9, 10, 11}   //  initializers for row indexed by 2
};
*/

#include <iostream>
using namespace std;

// function declaration:
double getAverage(int arr[], int size);
void changeArray(int arr[], int size);
void printArray(int arr[], int size);
void printArraybyPointer(int *arr, int size);
int main ()
{
   // an int array with 5 elements.
   int balance[5] = {1000, 2, 3, 17, 50};
   double avg;

   // pass pointer to the array as an argument.
   avg = getAverage( balance, 5 ) ;

   // output the returned value
   cout << "Average value is: " << avg << endl;

   changeArray(balance, 5);
   printArray(balance, 5);
   printArraybyPointer(balance, 5);
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

/*
* Here reference to arr[] is passed into the function
* Change the arr[] in the function will afffect the
* actual value of arr[] out of this function
* If change the 1st parameter to be "const int arr[]"
* then the content of arr[] can't be changed
*/
//void changeArray(const int arr[], int size)
void changeArray(int arr[], int size)
{
   int    i;

   for (i = 0; i < size; ++i)
   {
      arr[i]=100+i;
   }
   cout<<endl;
}

void printArray(int arr[], int size)
{
  cout<<"Enter printArray"<<endl;
  int    i = 0;
  for(i=0;i<size; i++)
  {
    cout<<"arr["<<i<<"] = "<< arr[i]<<endl;
  }
  cout<<"arr[-1] = "<< arr[-1]<<endl;
  cout<<endl;
}

void printArraybyPointer(int *arr, int size)
{
  cout<<"Enter printArraybyPointer"<<endl;
  int    i = 0;
  for(i=0;i<size; i++)
  {
    cout<<"arr["<<i<<"] = "<< arr[i]<<endl;
  }
  cout<<"arr[-1] = "<< arr[-1]<<endl;
  cout<<"arr[-2] = "<< arr[-2]<<endl;
  cout<<"arr[size+1] = "<< arr[size+1]<<endl;
  cout<<"address of arr[5] = "<< &arr[5]<<endl;
  cout<<"address of arr[4] = "<< &arr[4]<<endl;
  cout<<"address of arr[0] = "<< &arr[0]<<endl;
  cout<<"address of arr[-1] = "<< &arr[-1]<<endl;
  cout<<"address of arr[-2] = "<< &arr[-2]<<endl;
}
