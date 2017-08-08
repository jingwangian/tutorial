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
int *get_one_dim_array();
int **get_two_dim_array();
double getAverage(int arr[], int size);
void printArray(int arr[], int size);
void printArraybyPointer(int *arr, int size);
void print2dimArray(int **arr, int size_a, int size_b);
int main ()
{
   // an int array with 5 elements.
   int *balance=get_one_dim_array();
   int **two_dimarr = get_two_dim_array();
   double avg;

   // pass pointer to the array as an argument.
   avg = getAverage( balance, 5 ) ;

   // output the returned value
   cout << "Average value is: " << avg << endl;

   printArray(balance, 5);
   print2dimArray(two_dimarr,3,4);

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

int *get_one_dim_array()
{
  /*
  * static must be used here.
  * If using "int arr[]={1,2,3,4,5};"
  * the value of arr can't be fetched out of the function
  */
  static int arr[]={1,2,3,4,5};

  return arr;
}

int **get_two_dim_array()
{
  /*
  * static must be used here.
  * If using "int arr[]={1,2,3,4,5};"
  * the value of arr can't be fetched out of the function
  */
  static int a[3][4] = {
   {0, 1, 2, 3} ,   /*  initializers for row indexed by 0 */
   {4, 5, 6, 7} ,   /*  initializers for row indexed by 1 */
   {8, 9, 10, 11}   /*  initializers for row indexed by 2 */
};

  return (int**)a;
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

void print2dimArray(int **arr, int size_a, int size_b)
{
  cout<<"Enter print2dimArray"<<endl;
  int    i = 0;
  int    j = 0;
  for(i=0;i<size_a; i++)
  {
    for(j=0;j<size_b; j++)
    {
      cout<<"arr["<<i<<"]["<<j<<"] = "<< arr[i][j]<<endl;
    }
    cout<<endl;
  }
  cout<<endl;
}
